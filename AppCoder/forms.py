from django import forms
from .models import Alumno, Profesor, Curso, Entrega
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'especialidad', 'correo']

class EntregableForm(forms.ModelForm):
    comentario = forms.CharField(max_length=200, required=False, widget=forms.Textarea)

    class Meta:
        model = Entrega
        fields = ['archivo', 'comentario']

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']        
        help_text = {k:"" for k in fields}

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'edad', 'curso']
