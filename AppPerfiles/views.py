from django.shortcuts import render
from .models import Perfil
from django.http import HttpResponse
from django.urls import reverse_lazy
from AppPerfiles.forms import PerfilForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required #decorador para vistas basadas en funciones que permite que cambie un comportamiento cuando se está logueado
from django.contrib.auth.mixins import LoginRequiredMixin #decorador para vistas basadas en clases que permite que cambie un comportamiento cuando se está logueado


# Create your views here.


def home(request):
    return render (request, "AppBlog/home.html")


#................

@login_required #Solo permite acceder a la funcion y modificar lo que desee si estoy logueado
def leerPerfil(request):
    perfiles=Perfil.objects.all()
    return render (request, "AppPerfiles/leerPerfil.html", {"perfiles": perfiles})

@login_required #Solo permite acceder a la funcion y modificar lo que desee si estoy logueado
def agregarPerfil(request):
    if request.method=="POST":
        form= PerfilForm(request.POST) #por POST el formulario viene lleno
        
        if form.is_valid():
            informacion=form.cleaned_data #convierte la info en modo formulario a un diccionario más facil de leer
            
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            dni=informacion["dni"]
            email=informacion["email"]
            fecha_nacimiento=informacion["fecha_nacimiento"]                   
            perfil= Perfil(nombre=nombre, apellido=apellido, dni=dni, email= email, fecha_nacimiento=fecha_nacimiento)
            perfil.save()
            perfiles=Perfil.objects.all()
            return render (request, "AppPerfiles/leerPerfil.html", {"perfiles": perfiles, "mensaje": "Perfil guardado correctamente"})
        else:
            return render (request, "AppPerfiles/agregarPerfil.html", {"form": form, "mensaje": "Información no válida"})

    else: #sino viene por GET y el formulario viene vacío
        form= PerfilForm() #formulario vacío
        return render (request, "AppPerfiles/agregarPerfil.html", {"form": form})


@login_required #Solo permite acceder a la funcion y modificar lo que desee si estoy logueado
def editarPerfil(request, id):
    perfil=Perfil.objects.get(id=id)
    if request.method=="POST":
        form= PerfilForm(request.POST) #por POST el formulario viene lleno        
        if form.is_valid():
            info=form.cleaned_data #convierte la info en modo formulario a un diccionario más facil de leer
            perfil.nombre=info["nombre"]
            perfil.apellido=info["apellido"]
            perfil.dni=info["dni"]
            perfil.email=info["email"]
            perfil.fecha_nacimiento=info["fecha_nacimiento"]                  
            perfil.save()
            perfiles=Perfil.objects.all()
            return render (request, "AppPerfil/leerPerfiles.html", {"perfiles": perfiles, "mensaje": "Perfil editado correctamente"})
        pass
    else:
        form=PerfilForm(initial={"nombre":perfil.nombre, "apellido":perfil.apellido, "dni": perfil.dni, "email": perfil.email, "fecha_nacimiento": perfil.fecha_nacimiento})
        return render (request, "AppPerfil/editarPerfil.html", {"form": form, "perfil": perfil})


@login_required #Solo permite acceder a la funcion y modificar lo que desee si estoy logueado
def eliminarPerfil(request, id):
    perfil=Perfil.objects.get(id=id)
    perfil.delete()
    perfiles=Perfil.objects.all()
    return render (request, "AppPerfiles/leerPerfil.html", {"perfiles": perfiles, "mensaje": "Perfil eliminado correctamente"})


# @login_required #Solo permite acceder a la funcion y modificar lo que desee si estoy logueado
# def editarPerfil(request):
#     usuario=request.user

#     if request.method=="POST":
#         form= UserEditForm(request.POST) #por POST el formulario viene lleno        
#         if form.is_valid():
#             info=form.cleaned_data
#             usuario.email=info["email"]
#             usuario.password1=info["password1"]
#             usuario.password2=info["password2"] 
#             usuario.first_name=info["first_name"] 
#             usuario.last_name=info["last_name"]
#             usuario.save() #guardo en la base de datos el objeto que trae el formulario            
#             return render (request, "AppCoder/inicio.html", {"mensaje": f"Usuario {usuario.username} editado correctamente"})
#         else:
#             return render (request, "AppCoder/editarPerfil.html", {"form": form, "mensaje": "Error al editar el usuario"})

#     else: #sino viene por GET y el formulario viene vacío
#         form= UserEditForm(instance=usuario) #formulario vacío
#         return render (request, "AppCoder/editarPerfil.html", {"form": form, "nombreusuario": usuario.username})

