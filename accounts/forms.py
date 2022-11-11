from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MiFormularioDeCreación(UserCreationForm):
    
    email = forms.CharField()
    # username = forms.CharField(label='Usuario', max_length=20)        #Label es la designación que le pone al "username"
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)                    # El Widget es para que oculte los caracteres de la contraseña
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}                # LIST COMPRENSION: Permite generar por medio de un for un diccionario dinámico usando los datos anterior del field
        
class EditarPerfilFormulario(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)           # Incorpora el avatar al formulario
    description = forms.CharField(label='Descripcion')
    link = forms.CharField(label='Link')