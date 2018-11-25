# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):

    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):

    titulo = models.CharField(max_length=150)
    publicador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicaciones')
    contenido = models.TextField()
    categorias = models.ManyToManyField(Categoria, related_name='publicaciones')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):

    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    publicador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.publicador.username + ' [' + self.publicacion.titulo + ']'
