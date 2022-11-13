from distutils.log import Log
from django.shortcuts import redirect
from avanzado.models import Mascota
from avanzado.forms import BusquedaMascota

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def eliminar_mascota(request, id):
    
    mascota = Mascota.objects.get(id=id)
    
    mascota.delete()
    
    return redirect('ver_mascotas')

class ListaMascotas(ListView):
    model = Mascota
    template_name = 'avanzado/ver_mascotas_cbv.html'
    
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            object_list = self.model.objects.filter(nombre__icontains=nombre)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaMascota()
        return context
    
class CrearMascota(CreateView):
    model = Mascota
    success_url = '/avanzado/mascotas/'
    template_name = 'avanzado/crear_mascota_cbv.html'
    fields = ['nombre', 'tipo', 'edad_media_de_vida', 'fecha_de_creacion', 'descripcion', 'imagen']
    
class EditarMascota(LoginRequiredMixin, UpdateView):
    model = Mascota
    success_url = '/avanzado/mascotas/' 
    template_name = 'avanzado/editar_mascota_cbv.html'
    fields = ['nombre', 'tipo', 'edad_media_de_vida', 'fecha_de_creacion', 'descripcion', 'imagen']
  
class VerMascota(DetailView):
    model = Mascota
    template_name = 'avanzado/ver_mascota_cbv.html'