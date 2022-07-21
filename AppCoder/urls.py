from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('base/', base, name="base"),
    
    path('login', login_request, name="login"),
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
    path('editar_perfil', editar_perfil, name="editar_perfil"),
    path('agregar_avatar', agregar_avatar, name="agregar_avatar"),
    
    path('alumnos', alumnos, name="alumnos"),
    path('crearAlumno/', crearAlumno, name="crearAlumno"),
    path('buscarAlumno/', buscarAlumno, name="buscarAlumno"),
    path('eliminarAlumno/<alumno_id>', eliminarAlumno, name="eliminarAlumno"),
    path('editarAlumno/<alumno_id>', editarAlumno, name="editarAlumno"),
    
    path('profesores/list', ProfesList.as_view(), name="profe_list"),
    path('profesores/<pk>', ProfeDetail.as_view(), name="profe_detail"),
    path('profesor/nuevo', ProfeCreate.as_view(), name="profe_create"),
    path('profesores/editar/<pk>', ProfeUpdate.as_view(), name="profe_update"),
    path('profesores/eliminar/<pk>', ProfeDelete.as_view(), name="profe_delete"),
    
    path('crearCurso/', crearCurso, name="crearCurso"),
    path('cursos', cursos, name="cursos"),
    
    path('curso/list', CursosList.as_view(), name="curso_list"),
    path('curso/<pk>', CursoDetail.as_view(), name="curso_detail"),
    path('curso/nuevo', CursoCreate.as_view(), name="curso_create"),
    path('curso/editar/<pk>', CursoUpdate.as_view(), name="curso_update"),
    path('curso/eliminar/<pk>', CursoDelete.as_view(), name="curso_delete"),
]