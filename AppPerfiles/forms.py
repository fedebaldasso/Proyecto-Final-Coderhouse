from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PerfilForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50) #lo defino como un caracter de base de datos
    apellido=forms.CharField(label="Apellido", max_length=50) #lo defino como un entero de base de datos
    dni=forms.IntegerField(label="DNI")
    email=forms.EmailField(label="Email")
    fecha_nacimiento=forms.DateField(label= "Fecha de Nacimiento")
    tieneObraSocial=forms.BooleanField(label="Tiene Obra Social")

class UserEditForm(UserCreationForm): #nuestro formulario hereda de UserCreationForm
    email=forms.EmailField(label="Email")    
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')

    class Meta: #Configura el registro de Usuario
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts= {k:"" for k in fields} #borra las recomendaciones de llenado del formulario

