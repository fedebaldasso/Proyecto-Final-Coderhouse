from django.shortcuts import render
# from .models import Curso, Profesor, Estudiante, Persona, Avatar
from django.http import HttpResponse
from django.urls import reverse_lazy
from AppRegistro.forms import RegistroUsuarioForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required #decorador para vistas basadas en funciones que permite que cambie un comportamiento cuando se está logueado
from django.contrib.auth.mixins import LoginRequiredMixin #decorador para vistas basadas en clases que permite que cambie un comportamiento cuando se está logueado


# Create your views here.


def home(request):
    return render (request, "AppBlog/home.html")

#-------VISTA DE REGISTRO--------

def signup(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST) #por POST el formulario viene lleno        
        if form.is_valid():
            username=form.cleaned_data.get("username") 
            form.save() #guardo en la base de datos el objeto que trae el formulario            
            return render (request, "AppRegistro/signup.html", {"mensaje": f"Usuario {username} creado correctamente"})
        else:
            return render (request, "AppRegistro/signup.html", {"form": form, "mensaje": "Error al crear el usuario"})

    else: #sino viene por GET y el formulario viene vacío
        form= RegistroUsuarioForm() #formulario vacío
        return render (request, "AppRegistro/signup.html", {"form": form})


