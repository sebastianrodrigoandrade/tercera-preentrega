from django import forms

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

from .models import Entregable

class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['curso', 'nombre', 'descripcion', 'fecha_entrega', 'archivo']