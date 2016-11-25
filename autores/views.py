# coding=utf-8
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.views.generic.list import ListView

from .models import Autor


class CriarAutor(CreateView):
    model = Autor
    fields = ['first_name', 'last_name', 'email', 'username', 'password']
    template_name = 'criar-autor.html'
    success_url = '.'

    def form_valid(self, form):
        """
        Adiciona um password criptografado para o usuário
        """
        usuario = form.save(commit=False)
        usuario.set_password(form.cleaned_data['password'])
        usuario.save()
        return super(CriarAutor, self).form_valid(form)


# __ Substituido por def autores (melhor de explicar)
# class AutorList(ListView):
#     model = Autor
#     context_object_name = 'autores'  # nome da variável usada no html
#     template_name = 'autores.html'


def autores(request):
    """
    Retorna a lista de autores para a
    """
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores': autores})


def seguir(request, id=None):
    """
    Recebe o id do usuário que irá seguir
    """
    autor_seguir = Autor.objects.get(id=id)
    autor = request.user
    autor.seguindo.add(autor_seguir)  # .add adiciona na lista de seguindo
    autor.save()
    return redirect('autores')


def unfollow(request, id=None):
    """
    Recebe o id do usuário que irá seguir
    """
    autor_unfollow = Autor.objects.get(id=id)
    autor = request.user
    autor.seguindo.remove(autor_unfollow)  # .remove remove da lista de seguindo
    autor.save()
    return redirect('autores')


def excluir_autor(request, id=None):
    """
    Recebe o id do Autor e exclui
    """
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    return redirect('index')


def autor(request, id=None):
    """
    Recebe o autor pelo id e envia para a página autor.html
    """
    autor = get_object_or_404(Autor, id=id)
    return render(request, 'autor.html', {'autor': autor})
