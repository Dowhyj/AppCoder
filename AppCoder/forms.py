from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formularioAlumno(forms.Form):
    nombre = forms.CharField(max_length=30, label="Nombre")
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    
class formularioProfesor(forms.Form):
    nombre = forms.CharField(max_length=30, label="Nombre")
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    
class formularioCurso(forms.Form):
    nombre = forms.CharField(max_length=30)
    comision = forms.IntegerField()
    
class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}