from ast import Pass
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from accounts.forms import EditarPerfilFormulario, MiFormularioDeCreación
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ExtensionUsuario

# Create your views here.


def mi_login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            extensionUsuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user=request.user)
            return redirect('index')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'formulario': formulario})

def registrar(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreación(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('index')
    else:
        formulario = MiFormularioDeCreación()
        
    return render(request, 'accounts/registrar.html', {'formulario': formulario})

@login_required
def perfil(request):
    
    extensionUsuario, es_nuevo =ExtensionUsuario.objects.get_or_create(user=request.user)
    
    return render(request, 'accounts/perfil.html', {})

@login_required
def editar_perfil(request):
    
    user = request.user
    
    if request.method == 'POST':
        formulario = EditarPerfilFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            data_nueva = formulario.cleaned_data
            user.first_name = data_nueva['first_name']
            user.last_name = data_nueva['last_name']
            user.email = data_nueva['email']
            user.extensionusuario.avatar = data_nueva['avatar']
            user.description = data_nueva['description']
            user.link = data_nueva['link']
            
            user.extensionusuario.save()
            user.save()
            return redirect('perfil')

    else:
        formulario = EditarPerfilFormulario(
            initial={
                'first_name': request.user.first_name ,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'avatar': user.extensionusuario.avatar,
            }
        )
    formulario = EditarPerfilFormulario()
    return render(request, 'accounts/editar_perfil.html', {'formulario': formulario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/cambiar_contrasenia.html'
    success_url = '/accounts/perfil/'