from django.conf.urls import url

from autores import views
from autores.views import CriarAutor

urlpatterns = [
    url(r'^criar/$', CriarAutor.as_view(), name='criar_autor'),
    # url(r'^$', AutorList.as_view(), name='autores'),
    url(r'^$', views.autores, name='autores'),
    url(r'^(?P<id>\d+)/$', views.autor, name='autor'),
    url(r'^excluir/(?P<id>\d+)/$', views.excluir_autor, name='excluir_autor'),
    url(r'^seguir/(?P<id>\d+)/$', views.seguir, name='seguir_autor'),
    url(r'^unfollow/(?P<id>\d+)/$', views.unfollow, name='unfollow'),
]


