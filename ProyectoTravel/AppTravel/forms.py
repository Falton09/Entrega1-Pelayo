
from django import forms

class CreacionUsuarios(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class NuevoVuelo(forms.Form):
    destino = forms.CharField(max_length=40)
    fecha_salida = forms.DateField()
    fecha_regreso = forms.DateField()
    num_personas = forms.IntegerField()

class ReservaHotel(forms.Form):
    nombreH = forms.CharField(max_length=40)
    num_personas = forms.IntegerField()
    dia_entrada = forms.DateField()
    dia_salida = forms.DateField()

class BusquedaUsuarios(forms.Form):
    email = forms.EmailField()

class BusquedaVuelos(forms.Form):
    destino = forms.CharField(max_length=40)
    

class BusquedaResevas(forms.Form):
    nombreH = forms.CharField(max_length=40)
