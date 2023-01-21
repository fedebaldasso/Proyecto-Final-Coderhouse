from django.shortcuts import render
from .models import Blog, Avatar
from django.http import HttpResponse
from django.urls import reverse_lazy
from AppBlog.forms import PostForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required #decorador para vistas basadas en funciones que permite que cambie un comportamiento cuando se está logueado
from django.contrib.auth.mixins import LoginRequiredMixin #decorador para vistas basadas en clases que permite que cambie un comportamiento cuando se está logueado


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/avatarpordefecto.png"
    return avatar


# Create your views here.



def home(request):
    return render (request, "AppBlog/home.html")

def about(request):
    return render (request, "AppBlog/about.html")


def leerBlog(request):
    posteos=Blog.objects.all()
    return render (request, "AppBlog/pages.html", {"posteos": posteos})

@login_required #Solo permite acceder a la funcion y modificar lo que desee si estoy logueado
def agregarBlog(request):
    if request.method=="POST":
        form= PostForm(request.POST) #por POST el formulario viene lleno
        
        if form.is_valid():
            informacion=form.cleaned_data #convierte la info en modo formulario a un diccionario más facil de leer
            seccion=informacion["seccion"]
            titulo=informacion["titulo"]
            subtitulo=informacion["subtitulo"]
            contenido=informacion["contenido"]
            autor=informacion["autor"]
            fecha_publicacion=informacion["fecha_publicacion"]
            imagen=informacion["imagen"]            
            post= Blog(seccion=seccion, titulo=titulo, subtitulo=subtitulo, contenido=contenido, autor= autor, fecha_publicacion=fecha_publicacion, imagen=imagen )
            post.save()
            posteos=Blog.objects.all()
            return render (request, "AppBlog/pages.html", {"posteos": posteos, "mensaje": "Post guardado correctamente"})
        else:
            return render (request, "AppBlog/createPage.html", {"form": form, "mensaje": "Información no válida"})

    else: #sino viene por GET y el formulario viene vacío
        form= PostForm() #formulario vacío
        return render (request, "AppBlog/createPage.html", {"form": form})

@login_required #Solo permite acceder a la funcion y modificar lo que desee si estoy logueado
def editarBlog(request, id):
    post=Blog.objects.get(id=id)
    if request.method=="POST":
        form= PostForm(request.POST) #por POST el formulario viene lleno        
        if form.is_valid():
            info=form.cleaned_data #convierte la info en modo formulario a un diccionario más facil de leer
            post.seccion=info["seccion"]
            post.titulo=info["titulo"]
            post.subtitulo=info["subtitulo"]
            post.contenido=info["contenido"]
            post.autor=info["autor"]
            post.fecha_publicacion=info["fecha_publicacion"]
            post.imagen=info["imagen"]           
            post.save()
            posteos=Blog.objects.all()
            return render (request, "AppBlog/pages.html", {"posteos": posteos, "mensaje": "Post editado correctamente"})
        pass
    else:
        form=PostForm(initial={"seccion":post.seccion, "titulo":post.titulo, "subtitulo":post.subtitulo, "contenido":post.contenido, "autor": post.autor, "fecha_publicacion": post.fecha_publicacion, "imagen":post.imagen})
        return render (request, "AppBlog/updatePage.html", {"form": form, "post": post})

@login_required #Solo permite acceder a la funcion y modificar lo que desee si estoy logueado
def eliminarBlog(request, id):
    post=Blog.objects.get(id=id)
    post.delete()
    posteos=Blog.objects.all()
    return render (request, "AppBlog/pages.html", {"posteos": posteos, "mensaje": "Post eliminado correctamente"})

def detalleBlog(request, id):
    post=Blog.objects.get(id=id)
    return render (request, "AppBlog/detailPage.html", {"post": post})


def agregarAvatar(request):
    if request.method=="POST":
        form= AvatarForm(request.POST, request.FILES) #por POST el formulario viene lleno        
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user) #Se fija si ya tiene avatar y lo reemplaza por el nuevo
            if len(avatarViejo)>0:
                avatarViejo[0].delete()            
            avatar.save() #guardo en la base de datos el objeto que trae el formulario            
            return render (request, "AppBlog/inicio.html", {"mensaje": f"Avatar agregado correctamente"})
        else:
            return render (request, "AppBlog/agregarAvatar.html", {"form": form, "usuario":request.user, "mensaje": "Error al agregar el avatar"})

    else: #sino viene por GET y el formulario viene vacío
        form= AvatarForm() #formulario vacío
        return render (request, "AppBlog/agregarAvatar.html", {"form": form, "usuario": request.user})
