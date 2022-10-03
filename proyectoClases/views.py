from django.http import HttpResponse


from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template

def hola(request):
    return HttpResponse('<h1>Buenas tardes</h1>')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_actual}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad 
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años seria: {fecha}')

def mi_template(request):
    cargar_archivo = open(r'C:\Users\Ezequiel Walter\Dropbox (CGPBB)\Ezequiel Walter\Ezequiel Walter\Documentos\Ezequiel\Python\proyecto-clases\templates\template.html', 'r')
    template = Template(cargar_archivo.read())  #Cargar en memoria nuestro documento,template
    cargar_archivo.close()      #Cerramos el archivo
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)    #Renderizamos la plantilla del documento
    
    return HttpResponse(template_renderizado)