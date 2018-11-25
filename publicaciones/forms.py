from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from publicaciones.models import Publicacion, Categoria, Comentario
from django.contrib.auth.models import User

class PublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'categorias']

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nombre']

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['contenido']

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets={'password': forms.PasswordInput()}

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']

class UsuarioForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
