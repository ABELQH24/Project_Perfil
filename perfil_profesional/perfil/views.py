from django.shortcuts import render, redirect
from .models import Logro, Proyecto, Experiencia
from .forms import LogroForm, ProyectoForm, ExperienciaForm


# Create your views here.
def home(request):
    logros = Logro.objects.all()
    proyectos = Proyecto.objects.all()
    experiencias = Experiencia.objects.all()
    return render(request, 'home.html', {'logros':logros, 'proyectos': proyectos, 'experiencias':experiencias})

def agregar_logro(request):
    if request.method == 'POST':
        form = LogroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('logro_list')
    else:
        form = LogroForm()

    return render(request,'agregar_logro.html', {'form':form})


def agregar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        form = ProyectoForm
    return render(request, 'agregar_proyecto.html',{'form': form})
    
def agregar_experiencia(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST, request.FILE)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = ExperienciaForm
    return render(request, 'agregar_experiencia.html', {'form':form})
    