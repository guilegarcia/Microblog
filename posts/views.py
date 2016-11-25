# coding=utf-8
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

