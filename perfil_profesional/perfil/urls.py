from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('agregar_logro/', views.agregar_logro, name = 'agregar_logro'),
    path('agregar_proyecto/', views.agregar_proyecto, name = 'agregar_proyecto'),
    path('agregar_experiencia/', views.agregar_experiencia, name = 'agregar_experiencia'),
]
