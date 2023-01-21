from django.shortcuts import render
# from .models import Curso
from django.http import HttpResponse
from django.urls import reverse_lazy
# from AppLogin.forms import CursoForm, ProfeForm, PersonaForm, RegistroUsuarioForm, UserEditForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required #decorador para vistas basadas en funciones que permite que cambie un comportamiento cuando se está logueado
from django.contrib.auth.mixins import LoginRequiredMixin #decorador para vistas basadas en clases que permite que cambie un comportamiento cuando se está logueado


# Create your views here.

def home(request):
    return render (request, "AppBlog/home.html")


#-------VISTA DE LOGIN--------

def login_request(request):  # Creación de formulario
    if request.method=="POST":
        form= AuthenticationForm(request, data = request.POST) #por POST el formulario viene lleno
        
        if form.is_valid():
            info=form.cleaned_data #convierte la info en modo formulario a un diccionario más facil de leer
            
            usuario=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usuario, password=clave) #verifica si el usuario existe, si existe, lo devuelve, y sino devuelve None
            if usuario is not None:
                login(request, usuario)            
                return render (request, "AppLogin/login.html", {"mensaje": f"Usuario {usuario} logueado correctamente"})
            else:
                return render (request, "AppLogin/login.html", {"form": form, "mensaje": "Usuario o Contraseña incorrectos"})

        else: #sino viene por GET y el formulario viene vacío
            return render (request, "AppLogin/login.html", {"form": form, "mensaje": "Usuario o Contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render (request, "AppLogin/login.html", {"form": form})


