from re import template
from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView            # Es para el LogOut de la cuenta

urlpatterns = [
    path('login/', views.mi_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('registrar/', views.registrar, name='registrar'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar', views.editar_perfil, name='editar_perfil'),
    path('cambiar-contrasenia/', views.CambiarContrasenia.as_view(), name='cambiar_contrasenia'),            # Es una clase basada en vista
]
