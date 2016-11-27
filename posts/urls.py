from django.conf.urls import url

from posts import views
from posts.views import CriarPost

urlpatterns = [
    url(r'^criar/$', CriarPost.as_view(), name='criar_post'),
    # url(r'^excluir/(?P<id>\d+)/$', views.excluir_post, name='excluir_post'),
    url(r'^curtir/(?P<id>\d+)/$', views.curtir, name='curtir_post'),
]


