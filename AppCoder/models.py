import email
from django.db import models
from django.contrib.auth.models import User
    
class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    profesion = models.CharField(max_length=150, blank=True, null=True)
    curso = models.CharField(max_length=30, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Profesores"
        
