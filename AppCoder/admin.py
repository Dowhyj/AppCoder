from django.contrib import admin

from .models import *

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre','apellido')
    
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comision')
    search_fields = ('nombre', 'comision')
    
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre','apellido')
    
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Profesor, ProfesorAdmin)