from django.contrib import admin
from home.models import Familiar        # Importa Familiar desde los Models

# Register your models here.
admin.site.register(Familiar)           # Agrega Familiar dentro del acceso desde el Admin