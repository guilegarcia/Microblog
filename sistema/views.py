# coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from posts.models import Post


@login_required
def index(request):
    autor = request.user
    if autor.seguindo:  # None não funciona no filter (Se o usuário não seguir ninguém
        # Q = OR (sql)    __in (verifica uma lista)
        posts = Post.objects.filter(Q(autor__in=autor.seguindo.all()) | Q(autor=autor))
    else:
        posts = None
    return render(request, 'index.html', {'posts': posts})


def logar(request):
    """
    Faz o login
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Salva o usuário autenticado na session atual
            return redirect("index")
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('login')
