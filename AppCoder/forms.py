from django import forms

class formularioAlumno(forms.Form):
    nombre = forms.CharField(max_length=30, label="Nombre")
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()