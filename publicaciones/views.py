# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from publicaciones.models import Publicacion, Categoria, Comentario
from django.contrib.auth.models import User
from publicaciones.forms import PublicacionForm, CategoriaForm, ComentarioForm, LoginForm, RegistroForm, UsuarioForm
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

""" Publicaciones """

def listar_publicaciones(request):

    publicaciones = Publicacion.objects.all().order_by('-fecha')
    contexto = {'publicaciones': publicaciones}
    return render(request, 'publicaciones/listar_publicaciones.html', contexto)

def ver_publicacion(request, pk):

    publicacion = get_object_or_404(Publicacion, pk=pk)
    comentarios = Comentario.objects.filter(publicacion=publicacion).order_by('-fecha')

    contexto = {'publicacion': publicacion,
                'comentarios': comentarios,
                'formulario': crear_comentario(request, pk)}
    return render(request, 'publicaciones/ver_publicacion.html', contexto)

@staff_member_required
def crear_publicacion(request):

    if request.method == 'POST':

        publicacion = Publicacion()
        publicacion.publicador = request.user
        formulario = PublicacionForm(request.POST, instance=publicacion)

        if formulario.is_valid():

            formulario.save()
            formulario = PublicacionForm()
            messages.success(request, 'Publicación creada correctamente')
    else:
        formulario = PublicacionForm()

    contexto = {'formulario': formulario}
    return render(request, 'publicaciones/crear_publicacion.html', contexto)

@staff_member_required
def modificar_publicacion(request, pk):

    publicacion = get_object_or_404(Publicacion, pk=pk)

    if request.method == 'POST':

        formulario = PublicacionForm(request.POST, instance=publicacion)

        if formulario.is_valid():

            formulario.save()
            formulario = PublicacionForm(instance=publicacion)
            messages.success(request, 'Publicación modificada correctamente')
    else:
        formulario = PublicacionForm(instance=publicacion)

    contexto = {'formulario': formulario}
    return render(request, 'publicaciones/modificar_publicacion.html', contexto)

@staff_member_required
def borrar_publicacion(request, pk):

    publicacion = get_object_or_404(Publicacion, pk=pk)
    publicacion.delete()

    url = request.GET.get('next', 'listar-publicaciones')
    return redirect(url)

""" Categorias """

def listar_categorias(request):

    categorias = Categoria.objects.all()
    contexto = {'categorias': categorias}
    return render(request, 'categorias/listar_categorias.html', contexto)

def ver_categoria(request, pk):

    categoria = get_object_or_404(Categoria, pk=pk)
    publicaciones = Publicacion.objects.filter(categorias=categoria).order_by('-fecha')
    contexto = {'categoria': categoria,
                'publicaciones': publicaciones}
    return render(request, 'categorias/ver_categoria.html', contexto)

@staff_member_required
def crear_categoria(request):

    if request.method == 'POST':

        categoria = Categoria()
        formulario = CategoriaForm(request.POST, instance=categoria)

        if formulario.is_valid():

            formulario.save()
            formulario = CategoriaForm()
            messages.success(request, 'Categoría creada correctamente')
    else:
        formulario = CategoriaForm()

    contexto = {'formulario': formulario}
    return render(request, 'categorias/crear_categoria.html', contexto)

@staff_member_required
def modificar_categoria(request, pk):

    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':

        formulario = CategoriaForm(request.POST, instance=categoria)

        if formulario.is_valid():

            formulario.save()
            formulario = CategoriaForm(instance=categoria)
            messages.success(request, 'Categoría modificada correctamente')
    else:
        formulario = CategoriaForm(instance=categoria)

    contexto = {'formulario': formulario}
    return render(request, 'categorias/modificar_categoria.html', contexto)

@staff_member_required
def borrar_categoria(request, pk):

    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()

    url = request.GET.get('next', 'listar-categorias')
    return redirect(url)

""" Comentarios """

@login_required(login_url='iniciar-sesion')
def crear_comentario(request, pk):

    publicacion = get_object_or_404(Publicacion, pk=pk)

    if request.method == 'POST':

        comentario = Comentario()
        comentario.publicador = request.user
        comentario.publicacion = publicacion
        formulario = ComentarioForm(request.POST, instance=comentario)

        if formulario.is_valid():

            formulario.save()
            formulario = ComentarioForm()
            messages.success(request, 'Comentario publicado correctamente')
    else:
        formulario = ComentarioForm()

    return formulario

@staff_member_required
def borrar_comentario(request, pk):

    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.delete()

    url = request.GET.get('next', 'listar-publicaciones')
    return redirect(url)

""" Usuarios """

def listar_usuarios(request):

    usuarios = User.objects.all().order_by('-last_login')
    contexto = {'usuarios': usuarios}
    return render(request, 'usuarios/listar_usuarios.html', contexto)

def ver_usuario(request, pk):

    usuario = get_object_or_404(User, pk=pk)
    contexto = {'usuario': usuario}
    return render(request, 'usuarios/ver_usuario.html', contexto)

def iniciar_sesion(request):

    if request.method == 'POST':

        formulario = LoginForm(request.POST)

        if formulario.is_valid:
            username = request.POST['username']
            password = request.POST['password']

            usuario = authenticate(username=username, password=password)
            if usuario is None:
                messages.error(request, 'Usuario o contraseña incorrectos')
            else:
                login(request, usuario)
                url = request.GET.get('next', 'listar-publicaciones')
                return redirect(url)
    else:
        formulario = LoginForm()

    contexto = {'formulario': formulario}
    return render(request, 'usuarios/iniciar_sesion.html', contexto)

@login_required(login_url='iniciar-sesion')
def cerrar_sesion(request):
    logout(request)
    url = request.GET.get('next', 'listar-publicaciones')
    return redirect(url)

def registrar_usuario(request):

    if request.method == 'POST':

        formulario = RegistroForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            formulario = RegistroForm()
            messages.success(request, 'Usuario creado correctamente')
    else:
        formulario = RegistroForm()

    contexto = {'formulario': formulario}
    return render(request, 'usuarios/registrar_usuario.html', contexto)

@login_required(login_url='iniciar-sesion')
def modificar_usuario(request):

    if request.method == 'POST':

        formulario = UsuarioForm(request.POST, instance=request.user)

        if formulario.is_valid():

            formulario.save()
            formulario = UsuarioForm(instance=request.user)
            messages.success(request, 'Usuario modificado correctamente')
    else:
        formulario = UsuarioForm(instance=request.user)

    contexto = {'formulario': formulario}
    return render(request, 'usuarios/modificar_usuario.html', contexto)

@login_required(login_url='iniciar-sesion')
def cambiar_clave(request):

    if request.method == 'POST':

        formulario = PasswordChangeForm(request.user, request.POST)

        if formulario.is_valid():

            formulario.save()
            formulario = PasswordChangeForm(request.user)
            messages.success(request, 'Contraseña modificada correctamente')
    else:
        formulario = PasswordChangeForm(request.user)

    contexto = {'formulario': formulario}
    return render(request, 'usuarios/cambiar_clave.html', contexto)

@login_required(login_url='iniciar-sesion')
def borrar_usuario(request):

    request.user.delete()
    url = request.GET.get('next', 'listar-usuarios')
    return redirect(url)
