from django.urls import path
from avanzado import views

urlpatterns = [
    path('mascotas/eliminar/<int:id>', views.eliminar_mascota, name='eliminar_mascota'),
    path('mascotas/', views.ListaMascotas.as_view(), name='ver_mascotas'),
    path('mascotas/crear/', views.CrearMascota.as_view(), name='crear_mascota'),
    path('mascotas/editar/<int:pk>', views.EditarMascota.as_view(), name='editar_mascota'),
    path('mascotas/ver/<int:pk>', views.VerMascota.as_view(), name='ver_mascota'),
]
