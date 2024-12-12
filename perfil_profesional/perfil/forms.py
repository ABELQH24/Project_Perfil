from django import forms
from .models import Logro, Proyecto, Experiencia

class LogroForm(forms.ModelForm):
    class Meta:
        model = Logro
        fields = ['titulo', 'descripcion', 'archivo', 'imagen']

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre','descripcion', 'fecha','archivo','video']

class ExperienciaForm(forms.ModelForm):
    model = Experiencia
    fields = ['puesto', 'empresa','descripcion', 'inicio', 'fin' , 'foto']


