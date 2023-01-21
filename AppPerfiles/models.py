from django.db import models

# Create your models here.


class Perfil(models.Model):
    nombre= models.CharField(max_length=50) #lo defino como un caracter de base de datos
    apellido=models.CharField(max_length=50) #lo defino como un entero de base de datos
    dni=models.IntegerField()
    email=models.EmailField()
    fecha_nacimiento=models.DateField()
    