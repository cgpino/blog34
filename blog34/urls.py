"""blog34 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from publicaciones import views
from publicaciones.views import *

urlpatterns = [

    url(r'^$', views.listar_publicaciones, name='listar-publicaciones'),
    url(r'^publicacion/(?P<pk>\d+)', views.ver_publicacion, name='ver-publicacion'),
    url(r'^crear-publicacion', views.crear_publicacion, name='crear-publicacion'),
    url(r'^modificar-publicacion/(?P<pk>\d+)', views.modificar_publicacion, name='modificar-publicacion'),
    url(r'^borrar-publicacion/(?P<pk>\d+)', views.borrar_publicacion, name='borrar-publicacion'),

    url(r'^categorias', views.listar_categorias, name='listar-categorias'),
    url(r'^categoria/(?P<pk>\d+)', views.ver_categoria, name='ver-categoria'),
    url(r'^crear-categoria', views.crear_categoria, name='crear-categoria'),
    url(r'^modificar-categoria/(?P<pk>\d+)', views.modificar_categoria, name='modificar-categoria'),
    url(r'^borrar-categoria/(?P<pk>\d+)', views.borrar_categoria, name='borrar-categoria'),

    url(r'^borrar-comentario/(?P<pk>\d+)', views.borrar_comentario, name='borrar-comentario'),

    url(r'^usuarios', views.listar_usuarios, name='listar-usuarios'),
    url(r'^usuario/(?P<pk>\d+)', views.ver_usuario, name='ver-usuario'),
    url(r'^iniciar-sesion', views.iniciar_sesion, name='iniciar-sesion'),
    url(r'^cerrar-sesion', views.cerrar_sesion, name='cerrar-sesion'),
    url(r'^registrar-usuario', views.registrar_usuario, name='registrar-usuario'),
    url(r'^modificar-usuario', views.modificar_usuario, name='modificar-usuario'),
    url(r'^password', views.cambiar_clave, name='cambiar-clave'),
    url(r'^borrar-usuario', views.borrar_usuario, name='borrar-usuario'),

    url(r'^admin/', admin.site.urls),
]
