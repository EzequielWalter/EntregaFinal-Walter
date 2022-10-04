from unittest import loader
from django.http import HttpResponse


from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
from django.shortcuts import render
import random

from home.models import Familiar

def hola(request):
    return HttpResponse('<h1>Buenas tardes</h1>')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_actual}')

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

def crear_familiar(request, nombre, apellido):
    
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    
    familiar.save()
        
    # template = loader.get_template('crear_familiar.html')
    # template_renderizado = template.render({'familiar': familiar})
    # return HttpResponse(template_renderizado)
    
    return render(request, 'home/crear_familiar.html', {'familiar': familiar})

def ver_familiares(request):
    
    familiares = Familiar.objects.all()     # Le pide a la base de datos todos los objetos de Familiares
    
    # template = loader.get_template('ver_familiares.html')
    # template_renderizado = template.render({'familiares': familiares})
    # return HttpResponse(template_renderizado)
    
    return render(request, 'home/ver_familiares.html', {'familiares': familiares})       #Se puede poner asi como forma simplificada