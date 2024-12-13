from django.db import models

# Create your models here.
class Logro(models.Model):
    titulo = models.CharField(max_length = 230)
    descripcion = models.TextField() 
    archivo = models.FileField(upload_to = 'logros/', null = True, blank = True)
    imagen = models.ImageField(upload_to='logros_imagenes/', null = True, blank= True)

    def __str__(self):
        return self.titulo
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    archivo = models.FileField(upload_to = 'proyectos/', null = True, blank = True)
    video = models.FileField(upload_to='proyectos_videos/', null = True, blank = True)

    def __str__(self):  
        return self.nombre
    
class Experiencia(models.Model):
    puesto = models.CharField(max_length=250)
    empresa = models.CharField(max_length=250)
    descripcion = models.TextField()
    inicio = models.DateField()
    fin = models.DateField()
    foto = models.ImageField(upload_to='experiencia_fotos/', null = True, blank = True)

    def __str__(self):
        return f'{self.puesto} en la empresa {self.empresa}'
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contacto de {self.nombre} - {self.email}'