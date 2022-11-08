from django.urls import path
from home import views

urlpatterns = [
    # path('', views.index),
    path('', views.index, name='index'),        #Desgina nombre que se condice con los hipervinculos del index.html
    path('about/', views.about, name='about'),
    # path('hola/', views.hola),
    path('hola/', views.hola, name='hola'),
    # path('fecha/', views.fecha),
    path('fecha/', views.fecha, name='fecha'),
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    path('mi-template/', views.mi_template),
    path('mi-template/<str:nombre>', views.tu_template),
    path('prueba-template/', views.prueba_template),
    # path('ver-familiares/', views.ver_familiares),
    path('ver-familiares/', views.ver_familiares, name='ver_familiares'),
    path('crear-familiar/', views.crear_familiar, name='crear_familiar'),
]