# coding=utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.six import python_2_unicode_compatible


# @python_2_unicode_compatible # funcionar acentuação
# class Autor(models.Model):
#     nome = models.TextField(max_length=250)
#     username = models.TextField(max_length=250, unique=True)
#     senha = models.TextField(max_length=250)
#     seguindo = models.ForeignKey('self', blank=True, null=True)
#
#     def __str__(self):
#         return self.nome

class Autor(AbstractUser): # Herda do usuário comum do Django
    seguindo = models.ManyToManyField('self', blank=True)
    foto = models.ImageField(null=True, blank=True)




