from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('base/', base, name="base"),
    path('crearAlumno/', crearAlumno, name="crearAlumno")
]