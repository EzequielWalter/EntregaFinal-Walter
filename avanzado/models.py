from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    edad_media_de_vida = models.IntegerField()
    fecha_de_creacion = models.DateField()
    descripcion = RichTextField(null=True)                                       #Richtext

    def __str__(self):                                      # Sirve para poner los datos de la base de datos para mostarla desde el ADMIN
        return f'Nombre de raza: {self.nombre} - Tipo de animal: {self.tipo}'
    