from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(null=True)            # Es True para que pueda estar vacio
    
    def __str__(self):                                      # Sirve para poner los datos de la base de datos para mostarla desde el ADMIN
        return f'{self.nombre} {self.apellido}'