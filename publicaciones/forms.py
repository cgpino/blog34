from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from publicaciones.models import Publicacion, Categoria, Comentario
from django.contrib.auth.models import User

class PublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'imagen', 'categorias']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs['class'] = 'form-control'
        self.fields['contenido'].widget.attrs['class'] = 'form-control'
        self.fields['imagen'].widget.attrs['class'] = 'form-control'
        self.fields['categorias'].widget.attrs['class'] = 'form-control'

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['contenido']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['contenido'].widget.attrs['class'] = 'form-control'
        self.fields['contenido'].widget.attrs['rows'] = '3'

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets={'password': forms.PasswordInput()}

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

class UsuarioForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
