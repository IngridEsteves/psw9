# Generated by Django 5.0.2 on 2024-02-20 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='pergunta',
            field=models.TextField(),
        ),
    ]