from ast import Pass
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm    #Formulario de Django
from django.contrib.auth.forms import UserCreationForm      #Formulario de Django para Registrar usuarios
# from django.contrib.auth import login as django_login
from django.contrib.auth import login
from accounts.forms import EditarPerfilFormulario, MiFormularioDeCreación           # Importa en formulario que creamos en forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ExtensionUsuario

# Create your views here.


def mi_login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)     #Es la forma de hacerlo en el AuthenticationForm
        if formulario.is_valid():                       # Devuelve un True si el usuario/constraseña es correcto
            usuario = formulario.get_user()             # Devuelve el usuario del formulario
            login(request, usuario)
            # django_login(request, usuario)
            extensionUsuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user=request.user)  # Muestra la imagen del usuario
            return redirect('index')                    # Cuando inicia sesion lo manda a Index
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'formulario': formulario})

def registrar(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreación(request.POST)
        if formulario.is_valid():
            formulario.save()               # Crea directamente un usuario nuevo
            
            return redirect('index')                    # Cuando inicia sesion lo manda a Index
    else:
        formulario = MiFormularioDeCreación()
        
    return render(request, 'accounts/registrar.html', {'formulario': formulario})

@login_required
def perfil(request):
    
    extensionUsuario, es_nuevo =ExtensionUsuario.objects.get_or_create(user=request.user)          # Si extension usuario no existe, lo crea.
    
    return render(request, 'accounts/perfil.html', {})

@login_required
def editar_perfil(request):
    
    user = request.user
    
    if request.method == 'POST':
        formulario = EditarPerfilFormulario(request.POST, request.FILES)            # El request.FILES es para formularios que llevan imagen (avatar)
        
        if formulario.is_valid():
            data_nueva = formulario.cleaned_data
            user.first_name = data_nueva['first_name']
            user.last_name = data_nueva['last_name']
            user.email = data_nueva['email']
            user.extensionusuario.avatar = data_nueva['avatar']
            
            user.extensionusuario.save()
            user.save()                         # Hay dos save() porque son dos modelos distintos
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
    success_url = '/accounts/perfil/'    # Donde va despues de que se cambie la contraseña