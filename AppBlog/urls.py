from django.urls import path
from .views import *




urlpatterns = [
    
    path('', home, name="home"),

    path('about/', about, name="about"),

    path('pages/', leerBlog, name="pages"),
    path('createPage/', agregarBlog, name="createPage"),
    path('updatePage/<id>', editarBlog, name="updatePage"),
    path('deletePage/<id>', eliminarBlog, name="deletePage"),
    path('page/<id>', detalleBlog, name="page"),
    
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),




]