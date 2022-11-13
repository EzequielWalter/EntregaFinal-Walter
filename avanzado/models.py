from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    edad_media_de_vida = models.IntegerField()
    fecha_de_creacion = models.DateField()
    descripcion = RichTextField(null=True)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return f'Nombre de raza: {self.nombre} - Tipo de animal: {self.tipo}'
    