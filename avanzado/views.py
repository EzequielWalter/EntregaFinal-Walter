from distutils.log import Log
from django.shortcuts import render, redirect
from avanzado.models import Mascota
from avanzado.forms import MascotaFormulario, BusquedaMascota

from django.views.generic import ListView               # Para listar elementos
from django.views.generic.edit import CreateView        # Para crear
from django.views.generic.edit import UpdateView        # Para Ediar
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView             # Vista de detalle

from django.contrib.auth.mixins import LoginRequiredMixin     # Sirve para esconder parte de la información de la pagina si no está logueado (para CBV)
from django.contrib.auth.decorators import login_required     # Los decoradores es una funcionalidad para cubrir información. Es para cuando no es CBV
# Create your views here.

def ver_mascotas(request):
    
    mascotas = Mascota.objects.all()         # Trae todos los objetos del modelo Mascota
    
    return render(request, 'avanzado/ver_mascotas.html', {'mascotas': mascotas})

@login_required             # Protege la información que se encuentra por debajo (crear mascota)
def crear_mascota(request):
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST) 
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            mascota = Mascota(
                nombre=datos['nombre'],
                tipo=datos['tipo'],
                edad=datos['edad'],
                fecha_nacimiento=datos['fecha_nacimiento']
            )
            mascota.save()
            return redirect('ver_mascotas')
        else:
            return render(request, 'avanzado/crear_mascota.html', {'formulario': formulario})
    
    formulario = MascotaFormulario()    
    
    return render(request, 'avanzado/crear_mascota.html', {'formulario': formulario})

def editar_mascota(request, id):
    
    mascota = Mascota.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST) 
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            mascota.nombre = datos['nombre']
            mascota.tipo = datos['tipo']
            mascota.edad = datos['edad']
            mascota.fecha_nacimiento = datos['fecha_nacimiento']
            mascota.save()
            return redirect('ver_mascotas')
        else:
            return render(request, 'avanzado/editar_mascota.html', {'formulario': formulario})
    
    formulario = MascotaFormulario(
        initial={
            'nombre': mascota.nombre, 
            'tipo': mascota.tipo,
            'edad': mascota.edad,
            'fecha_nacimiento': mascota.fecha_nacimiento
        }
    )    
    
    return render(request, 'avanzado/editar_mascota.html', {'formulario': formulario, 'mascota': mascota})

def eliminar_mascota(request, id):
    
    mascota = Mascota.objects.get(id=id)
    
    mascota.delete()
    
    return redirect('ver_mascotas')



class ListaMascotas(ListView):
    model = Mascota
    template_name = 'avanzado/ver_mascotas_cbv.html'
    
    def get_queryset(self):
        test = self.request.GET.get('nombre', '')
        if test:
            object_list = self.model.objects.filter(nombre_icontains=nombre)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaMascota()
        return context
    
class CrearMascota(CreateView):
    model = Mascota
    success_url = '/avanzado/mascotas/'                         #Direccion a la cual accede cuando se crea (idem Redirect)
    template_name = 'avanzado/crear_mascota_cbv.html'           #Template al que va  
    fields = ['nombre', 'tipo', 'edad', 'fecha_nacimiento', 'descripcion']     #Campos que queremos que el elementos muestre el formulario (sale de lo que hay en el Modelo)
    
class EditarMascota(UpdateView):
    model = Mascota
    success_url = '/avanzado/mascotas/' 
    template_name = 'avanzado/editar_mascota_cbv.html'
    fields = ['nombre', 'tipo', 'edad', 'fecha_nacimiento', 'descripcion']
        
class EliminarMascota(LoginRequiredMixin, DeleteView):              # El LoginRequiredMixin va al principio
    model = Mascota
    success_url = '/avanzado/mascotas/'
    template_name = 'avanzado/eliminar_mascota_cbv.html'
    
class VerMascota(DetailView):
    model = Mascota
    template_name = 'avanzado/ver_mascota_cbv.html'