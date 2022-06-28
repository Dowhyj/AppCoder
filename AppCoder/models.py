import email
from django.db import models
    
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
    
    class Meta:
        verbose_name_plural = "Profesores"