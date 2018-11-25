# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from publicaciones.models import Publicacion, Categoria, Comentario

admin.site.register(Publicacion)
admin.site.register(Categoria)
admin.site.register(Comentario)
