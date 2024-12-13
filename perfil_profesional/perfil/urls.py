from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('agregar_logro/', views.agregar_logro, name = 'agregar_logro'),
    path('agregar_proyecto/', views.agregar_proyecto, name = 'agregar_proyecto'),
    path('agregar_experiencia/', views.agregar_experiencia, name = 'agregar_experiencia'),

    path('logro_list/', views.logro_list, name='logros'),
    #path('proyectos/', views.proyectos, name='proyectos'),
    #path('experiencia/', views.experiencia, name='experiencia'),

    path('eliminar_logro/<int:logro_id>/', views.eliminar_logro, name='eliminar_logro'),  # Ruta para eliminar logros
    # Otras rutas que tengas definidas
]

