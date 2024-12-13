from django import forms
from .models import Logro, Proyecto, Experiencia, Contacto

class LogroForm(forms.ModelForm):
    class Meta:
        model = Logro
        fields = ['titulo', 'descripcion', 'archivo', 'imagen']

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre','descripcion', 'fecha','archivo','video']
        widgets = {
            'fecha':forms.DateInput(attrs = {'type':'date'})
        }

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['puesto', 'empresa','descripcion', 'inicio', 'fin' , 'foto']
        widgets = {
            'inicio': forms.DateInput(attrs = {'type':'date'}),
            'fin': forms.DateInput(attrs={'type':'date'})
        }

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']

