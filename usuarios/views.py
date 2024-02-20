from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth


# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.WARNING, 'As senhas não coincidem')
            return redirect('/usuarios/cadastro')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.WARNING, 'Já existe um usuário com o mesmo username')
            return redirect('/usuarios/cadastro')

        try:
            user = User.objects.create_user(
                first_name=nome,
                username=username,
                password=confirmar_senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso.')
            return redirect('/usuarios/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/usuarios/cadastro')


def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)
        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado!')
            return redirect('/flashcard/novo_flashcard/')
        else:
            messages.add_message(
                request, constants.ERROR, 'Username ou senha inválidos'
            )
            return redirect('/usuarios/login')
