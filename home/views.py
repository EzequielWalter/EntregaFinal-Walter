from unittest import loader
from django.http import HttpResponse


from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random
from home.forms import BusquedaFamiliarFormulario, FamiliarFormulario

from home.models import Familiar

def hola(request):
    return HttpResponse('<h1>Buenas tardes</h1>')      # Agregando el ancla vuelve al Index

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_actual}')

def about(request):
    
    return render(request, 'home/about.html')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad 
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años seria: {fecha}')

def mi_template(request):
    cargar_archivo = open(r'C:\Users\Ezequiel Walter\Dropbox (CGPBB)\Ezequiel Walter\Ezequiel Walter\Documentos\Ezequiel\Python\proyecto-clases\home\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read())  #Cargar en memoria nuestro documento,template
    cargar_archivo.close()      #Cerramos el archivo
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)    #Renderizamos la plantilla del documento
    
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    template = loader.get_template('home/tu_template.html')
    
    template_renderizado = template.render({'persona': nombre})
    
    return HttpResponse(template_renderizado)

def prueba_template(request):
    
    mi_contexto = {
        'rango': list(range(1,11)),
        'valor_aleatorio': random.randrange(1,11)
    }
        
    template = loader.get_template('home/prueba_template.html')
    
    template_renderizado = template.render(mi_contexto)
    
    return HttpResponse(template_renderizado)

# def crear_familiar(request, nombre, apellido):
    
#     familiar = Familiar(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    
#     familiar.save()
        
#     # template = loader.get_template('crear_familiar.html')
#     # template_renderizado = template.render({'familiar': familiar})
#     # return HttpResponse(template_renderizado)
    
#     return render(request, 'home/crear_familiar.html', {'familiar': familiar})

def crear_familiar(request):
    
    if request.method == 'POST':        # Se asegura de que el formulario entre por POST
        
        formulario = FamiliarFormulario(request.POST)
        
        if formulario.is_valid():        # Chequea que el formulario esa correcto
            data = formulario.cleaned_data     #Le pide la información limpia al formulario
            
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            # fecha_nacimiento = data.get('fecha_nacimiento', datetime.now())     #Si no hay fecha de nacimiento ingresada pone la de ahora
            
            #v1
            fecha_creacion = data['fecha_creacion']
            if not fecha_creacion:
                fecha_creacion = datetime.now()
            
            #v2
            # fecha_creacion = data['fecha_creacion'] or datetime.now()
            
            
            familiar = Familiar(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_creacion=fecha_creacion)
            familiar.save()
        
        return redirect('ver_familiares')   # redirige a ver los familiares
    
    formulario = FamiliarFormulario()       # Hago la variable formulario traida de familiar
    
    return render(request, 'home/crear_familiar.html', {'formulario': formulario})  # Paso el formulario como contexto

def ver_familiares(request):
    
    nombre = request.GET.get('nombre')  # Es para buscar por nombre
    
    if nombre:
        familiares = Familiar.objects.filter(nombre__icontains=nombre)     #Filtra todos los que tengan nombre aunque no esté escrita toda la palabra
    else:
        familiares = Familiar.objects.all()     # Le pide a la base de datos todos los objetos de Familiares
    
    # template = loader.get_template('ver_familiares.html')
    # template_renderizado = template.render({'familiares': familiares})
    # return HttpResponse(template_renderizado)
    
    formulario = BusquedaFamiliarFormulario()
    
    return render(request, 'home/ver_familiares.html', {'familiares': familiares, 'formulario': formulario})       #Se puede poner asi como forma simplificada

def index(request):
    
    return render(request, 'home/index.html')