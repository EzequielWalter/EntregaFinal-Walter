from django import forms    #Para crear formularios


class FamiliarFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)    # False para que pueda estar vacio este campo
    
class BusquedaFamiliarFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)