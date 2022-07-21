from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Avatar

class AvatarForm(forms.Form):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']

class formularioAlumno(forms.Form):
    nombre = forms.CharField(max_length=30, label="Nombre")
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    
class formularioProfesor(forms.Form):
    nombre = forms.CharField(max_length=30, label="Nombre")
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=150)
    curso = forms.CharField(max_length=30)
    
class formularioCurso(forms.Form):
    nombre = forms.CharField(max_length=30)
    comision = forms.IntegerField()
    
class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}