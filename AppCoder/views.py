from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.

def index(request):
    return render(request, 'AppCoder/index.html',)

def base(request):
    return render(request, 'AppCoder/base.html',{})

def crearAlumno(request):
    
    if request.method == "POST":
    
        formulario = formularioAlumno(request.POST)
        
        if formulario.is_valid():
            
            info_alumno = formulario.cleaned_data
            
            alumno = Alumno(nombre=info_alumno["nombre"], apellido=info_alumno["apellido"], email=info_alumno["email"])
            
            alumno.save()
            
            return redirect('crearAlumno')
        
        else:
            
            return render(request,"AppCoder/form_crear_alumno.html",{"form":formulario})
        
    else:
        
        formularioVacio = formularioAlumno()
        
        return render(request,"AppCoder/form_crear_alumno.html",{"form":formularioVacio})