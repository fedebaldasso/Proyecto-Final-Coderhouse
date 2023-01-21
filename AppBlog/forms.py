from django import forms
from django.forms import ModelForm
from.models import Blog

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['seccion', 'titulo', 'subtitulo', 'contenido', 'autor', 'fecha_publicacion', 'imagen']
    

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
