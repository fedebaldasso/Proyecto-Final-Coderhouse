from django.urls import path
from .views import *




urlpatterns = [
    
    path('', home, name="home"), 

    # path('pages/', leerBlog, name="pages"),
    # path('createPage/', agregarBlog, name="createPage"),
    # path('updatePage/<id>', editarBlog, name="updatePage"),
    # path('deletePage/<id>', eliminarBlog, name="deletePage"),    
    
    




]