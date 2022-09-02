from django.shortcuts import render, redirect
from AppTravel.forms import CreacionUsuarios
from AppTravel.models import Usuario
from django.contrib import messages

def inicio(request):
    if request.method == 'POST':
        mi_formulario = CreacionUsuarios(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            usuario1 = Usuario(nombre=data.get('nombre'), apellido=data.get('apellido'), email=data.get('email'))
            usuario1.save()

            return redirect('AppTravelEstadia')
        
            
    
    contexto = {
        'form': CreacionUsuarios()
    }
   
    return render(request, 'index.html',contexto)


def vuelo(request):

    if request.method == 'POST':
        mi_formulario = CreacionUsuarios(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            usuario1 = Usuario(nombre=data.get('nombre'), apellido=data.get('apellido'), email=data.get('email'))
            usuario1.save()

            return redirect('AppTravelVuelos')
        
            
    
    contexto = {
        'form': CreacionUsuarios()
    }


    return render(request, 'AppTravel/vuelos.html')



