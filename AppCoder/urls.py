from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('base/', base, name="base"),
    
    path('crearAlumno/', crearAlumno, name="crearAlumno"),
    path('crearProfesor/', crearProfesor, name="crearProfesor"),
    path('crearCurso/', crearCurso, name="crearCurso"),
    
    path('buscarAlumno/', buscarAlumno, name="buscarAlumno"),
]