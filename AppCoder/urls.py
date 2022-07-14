from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('base/', base, name="base"),
    
    path('login', login_request, name="login"),
    
    
    path('alumnos', alumnos, name="alumnos"),
    path('crearAlumno/', crearAlumno, name="crearAlumno"),
    path('buscarAlumno/', buscarAlumno, name="buscarAlumno"),
    path('eliminarAlumno/<alumno_id>', eliminarAlumno, name="eliminarAlumno"),
    path('editarAlumno/<alumno_id>', editarAlumno, name="editarAlumno"),
    
    
    path('profesores', profesores, name="profesores"),
    path('crearProfesor/', crearProfesor, name="crearProfesor"),
    
    
    path('crearCurso/', crearCurso, name="crearCurso"),
    path('cursos', cursos, name="cursos"),
    
    path('curso/list', CursosList.as_view(), name="curso_list"),
    path(r'^(?P<pk>\d+)$', CursoDetail.as_view(), name="curso_detail"),
    path(r'^nuevo$', CursoCreate.as_view(), name="curso_create"),
    path(r'^editar/(?P<pk>\d+)$', CursoUpdate.as_view(), name="curso_update"),
    path(r'^eliminar/(?P<pk>\d+)$', CursoDelete.as_view(), name="curso_delete"),
    
]