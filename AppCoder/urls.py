from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('base/', base, name="base"),
    
    path('crearAlumno/', crearAlumno, name="crearAlumno"),
    path('crearProfesor/', crearProfesor, name="crearProfesor"),
    path('crearCurso/', crearCurso, name="crearCurso"),
    
    path('alumnos', alumnos, name="alumnos"),
    path('profesores', profesores, name="profesores"),
    path('cursos', cursos, name="cursos"),
    
    path('buscarAlumno/', buscarAlumno, name="buscarAlumno"),
]