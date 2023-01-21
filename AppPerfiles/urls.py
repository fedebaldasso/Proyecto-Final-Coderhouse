from django.urls import path
from .views import *



urlpatterns = [
    
    path('', home, name="home"),    

    path('leerPerfil/', leerPerfil, name="leerPerfil"),
    path('agregarPerfil/', agregarPerfil, name="agregarPerfil"),
    path('editarPerfil/<id>', editarPerfil, name="editarPerfil"),
    path('eliminarPerfil/<id>', eliminarPerfil, name="eliminarPerfil"),


]