from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Flashcard(models.Model):
    DIFICULDADE_CHOICES = (('1', 'Semana 1'), ('2', 'Semana 2'), ('3', 'Semana 3'), ('4', 'Semana 4'), ('5', 'Semana 5'), ('6', 'Semana 6'), ('7', 'Semana 7'))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pergunta = models.TextField()
    resposta = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    dificuldade = models.CharField(max_length=1, choices=DIFICULDADE_CHOICES)

    def __str__(self):
        return self.pergunta


class FlashcardDesafio(models.Model):
    flashcard = models.ForeignKey(Flashcard, on_delete=models.DO_NOTHING)
    respondido = models.BooleanField(default=False)
    acertou = models.BooleanField(default=False)

    def __str__(self):
        return self.flashcard.pergunta


class Desafio(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=100)
    categoria = models.ManyToManyField(Categoria)
    quantidade_perguntas = models.IntegerField()
    dificuldade = models.CharField(
        max_length=1, choices=Flashcard.DIFICULDADE_CHOICES
    )
    flashcards = models.ManyToManyField(FlashcardDesafio)

    def __str__(self):
        return self.titulo
