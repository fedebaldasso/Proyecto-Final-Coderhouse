from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):
    seccion=models.CharField(max_length=50)
    titulo= models.CharField(max_length=500) 
    subtitulo=models.CharField(max_length=500) 
    contenido=RichTextField(blank=True, null=True) 
    autor= models.CharField(max_length=50)    
    fecha_publicacion=models.DateField()
    imagen= RichTextUploadingField(blank=True, null=True)


    def __str__(self):
        return f"{self.titulo} {str(self.autor)}"


class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user= models.ForeignKey(User, on_delete=models.CASCADE) #Hace la conexión del avatar con el usuario

    def __str__(self):
        return f"{self.user} {str(self.imagen)}"
    