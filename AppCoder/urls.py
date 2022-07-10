from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('base/', base, name="base"),
    
    
    path('alumnos', alumnos, name="alumnos"),
    path('crearAlumno/', crearAlumno, name="crearAlumno"),
    path('buscarAlumno/', buscarAlumno, name="buscarAlumno"),
    path('eliminarAlumno/<alumno_id>', eliminarAlumno, name="eliminarAlumno"),
    path('editarAlumno/<alumno_id>', editarAlumno, name="editarAlumno"),
    
    
    path('profesores', profesores, name="profesores"),
    path('crearProfesor/', crearProfesor, name="crearProfesor"),
    
    
    path('crearCurso/', crearCurso, name="crearCurso"),
    path('cursos', cursos, name="cursos"),
    
    
]