from django.shortcuts import render, redirect, get_object_or_404
from .models import Logro, Proyecto, Experiencia
from .forms import LogroForm, ProyectoForm, ExperienciaForm


# Create your views here.
def home(request):
    logros = Logro.objects.all()
    proyectos = Proyecto.objects.all()
    experiencias = Experiencia.objects.all()
    
    context = {
        "logros": logros,
        "proyectos": proyectos,
        "experiencias": experiencias,
    }
    
    return render(request, 'home.html', context)

def logro_list(request):
    logros = Logro.objects.all()
    return render(request, 'logro_list.html', {'logros': logros})

def agregar_logro(request):
    if request.method == 'POST':
        form = LogroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('logros')
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

        form = ProyectoForm()
    return render(request, 'agregar_proyecto.html',{'form': form})
    
def agregar_experiencia(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExperienciaForm()
    return render(request, 'agregar_experiencia.html', {'form':form})

def contacto(request):
    if request.method == "POST":
        # Procesar el formulario de contacto
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        # Aquí podrías agregar lógica para enviar un correo electrónico o guardar el mensaje en la base de datos
        return render(request, 'contacto_gracias.html', {"nombre": nombre})
    return render(request, 'contacto.html')

def eliminar_logro(request, logro_id):
    logro = get_object_or_404(Logro, id=logro_id)
    if request.method == 'POST':
        logro.delete()
        return redirect('logros')
    return render(request, 'logros')