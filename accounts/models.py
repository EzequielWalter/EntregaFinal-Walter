from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExtensionUsuario(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)   # El campo puede estar vacío y el campo se puede vaciar
    # user = models.ForeignKey(User, on_delete=models.CASCADE)              # ForenignKey es un campo que está relacionado a un dato del model que le digamos
    user = models.OneToOneField(User, on_delete=models.CASCADE)             # OnetoOneField permite relacionar un objeto del modelo a un usuario
    