from django.shortcuts import render, redirect

from .forms import *
from .models import *

from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def index(request):
    return render(request, 'AppCoder/index.html',)

def base(request):
    return render(request, 'AppCoder/base.html',{})


def alumnos(request):
    
    if request.method=="POST":
        
        search = request.POST["search"]
        
        if search != "":
            
            alumnos = Alumno.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search)).values()
            
            return render(request,"AppCoder/alumnos.html",{"alumnos":alumnos, "search":True, "busqueda":search})
    
    alumnos = Alumno.objects.all()
    
    return render(request, 'AppCoder/alumnos.html',{"alumnos":alumnos})

def crearAlumno(request):
    
    if request.method == "POST":
    
        formulario = formularioAlumno(request.POST)
        
        if formulario.is_valid():
            
            info_alumno = formulario.cleaned_data
            
            alumno = Alumno(nombre=info_alumno["nombre"], apellido=info_alumno["apellido"], email=info_alumno["email"])
            
            alumno.save()
            
            return redirect('alumnos')
        
        else:
            
            return render(request,"AppCoder/form_crear_alumno.html",{"form":formulario})
        
    else:
        
        formularioVacio = formularioAlumno()
        
        return render(request,"AppCoder/form_crear_alumno.html",{"form":formularioVacio})

def buscarAlumno(request):
    
    if request.method == "POST":
        
        alumno = request.POST["alumno"]    

        alumnos = Alumno.objects.filter( Q(nombre__icontains=alumno) | Q(apellido__icontains=alumno) ).values()
        
        return render(request,"AppCoder/buscar_alumno.html",{"alumnos":alumnos})
    
    else: 
        
        alumnos = []

        return render(request,"AppCoder/buscar_alumno.html",{"alumnos":alumnos})

def eliminarAlumno(request, alumno_id):
    
    alumno = Alumno.objects.get(id=alumno_id)
    alumno.delete()
    
    return redirect("alumnos")

def editarAlumno(request, alumno_id):
    
    alumno = Alumno.objects.get(id=alumno_id)
    
    if request.method == "POST":
        
        formulario = formularioAlumno(request.POST)
        
        if formulario.is_valid():
            
            info_alumno = formulario.cleaned_data
            alumno.nombre = info_alumno["nombre"]
            alumno.apellido = info_alumno["apellido"]
            alumno.email = info_alumno["email"]
            alumno.save()
            
            return redirect("alumnos")
        
    formulario = formularioAlumno(initial={"nombre":alumno.nombre, "apellido":alumno.apellido, "email": alumno.email})
    
    return render(request,"AppCoder/form_crear_alumno.html",{"form":formulario})


def profesores(request):
    
    profesores = Profesor.objects.all()
    
    ctx = {"profesores":profesores}
    
    return render(request, 'AppCoder/profesores.html',ctx)

def crearProfesor(request):
    
    if request.method == "POST":
    
        formulario = formularioProfesor(request.POST)
        
        if formulario.is_valid():
            
            info_profesor = formulario.cleaned_data
            
            profesor = Profesor(nombre=info_profesor["nombre"], apellido=info_profesor["apellido"], email=info_profesor["email"])
            
            profesor.save()
            
            return redirect('crearProfesor')
        
        else:
            
            return render(request,"AppCoder/form_crear_profesor.html",{"form":formulario})
        
    else:
        
        formularioVacio = formularioProfesor()
        
        return render(request,"AppCoder/form_crear_profesor.html",{"form":formularioVacio})



def cursos(request):
    
    cursos = Curso.objects.all
    
    ctx = {"cursos":cursos}
    
    return render(request, 'AppCoder/cursos.html',ctx)
    
def crearCurso(request):
    
    if request.method == "POST":
    
        formulario = formularioCurso(request.POST)
        
        if formulario.is_valid():
            
            info_curso = formulario.cleaned_data
            
            curso = Curso(nombre=info_curso["nombre"], comision=info_curso["comision"])
            
            curso.save()
            
            return redirect('crearCurso')
        
        else:
            
            return render(request,"AppCoder/form_crear_curso.html",{"form":formulario})
        
    else:
        
        formularioVacio = formularioCurso()
        
        return render(request,"AppCoder/form_crear_curso.html",{"form":formularioVacio})
    
class CursosList(ListView):
    
    model = Curso
    template_name = "AppCoder/cursos_list.html"
    
class CursoDetail(DetailView):
    
    model = Curso
    template_name = "AppCoder/curso_detail.html"
    
class CursoCreate(CreateView):
    
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ["nombre", "comision"]
    
class CursoUpdate(UpdateView):
    
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ["nombre", "comision"]
    
class CursoDelete(DeleteView):
    
    model = Curso
    success_url = "/AppCoder/curso/list"