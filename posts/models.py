from django.db import models

from autores.models import Autor


class Post(models.Model):
    texto = models.TextField(max_length=140)
    likes = models.IntegerField(default=0, null=True, blank=True)
    autor = models.ForeignKey(Autor, null=True, blank=True)
    data_hora = models.DateTimeField(auto_now_add=True)
