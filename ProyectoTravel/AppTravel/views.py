from django.shortcuts import render, redirect
from AppTravel.forms import CreacionUsuarios, NuevoVuelo, ReservaHotel
from AppTravel.models import Hotel, Usuario, Vuelos
from django.contrib import messages

def inicio(request):
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
   
    return render(request, 'index.html',contexto)


def vuelo(request):

    if request.method == 'POST':
        mi_formulario = NuevoVuelo(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            vuelo1 = Vuelos(destino=data.get('destino'), fecha_salida=data.get('fecha_salida'), fecha_regreso=data.get('fecha_regreso'), num_personas=data.get('num_personas'))
            vuelo1.save()

            

            return redirect('AppTravelVuelos')

            
        
            
    
    contexto = {
        'form': NuevoVuelo()
    }


    return render(request, 'AppTravel/vuelos.html',contexto)


def reserva_hotel(request):

    if request.method == 'POST':
        mi_formulario = ReservaHotel(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            vuelo1 = Hotel(nombreH=data.get('nombreH'), num_personas=data.get('num_personas'), dia_entrada=data.get('dia_entrada'), dia_salida=data.get('dia_salida'))
            vuelo1.save()

        
        
            
    
    contexto = {
        'form': ReservaHotel()
    }


    return render(request, 'AppTravel/reserva_hotel.html',contexto)




