# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

from autores.models import Autor
from .models import Post

class CriarPost(CreateView):
    model = Post
    fields = ['texto']
    template_name = 'criar-post.html'
    success_url = '.'

    def form_valid(self, form): # TODO inserir o autor diretamente no <form {{request.user }}
        """
        Adiciona o usuário logado como autor do Post
        """
        post = form.save(commit=False)
        post.autor = self.request.user
        post.save()
        return super(CriarPost, self).form_valid(form)


def excluir_post(request, id=None):
    """
    Recebe o id do Post e exclui
    """
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('index')


@login_required
def index(request):
    autor = request.user
    if autor.seguindo:  # None não funciona no filter (Se o usuário não seguir ninguém
        # Q = OR (sql)    __in (verifica uma lista)
        posts = Post.objects.filter(Q(autor__in=autor.seguindo.all()) | Q(autor=autor))
    else:
        posts = None
    return render(request, 'index.html', {'posts': posts})

