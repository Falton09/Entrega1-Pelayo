from django.shortcuts import render, redirect
from AppTravel.forms import BusquedaUsuarios, CreacionUsuarios, NuevoVuelo, ReservaHotel
from AppTravel.models import Hotel, Usuario, Vuelos

#inicio de la pagina, va hacer un login para que la informacion se entrelace
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

#se crea el formulario de Vuelo del usuario
def vuelo(request):

    if request.method == 'POST':
        mi_formulario = NuevoVuelo(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            vuelo1 = Vuelos(destino=data.get('destino'), fecha_salida=data.get('fecha_salida'), fecha_regreso=data.get('fecha_regreso'), num_personas=data.get('num_personas'))
            vuelo1.save()

            return redirect('AppTravelReservaHotel')
         
    contexto = {
        'form': NuevoVuelo()
    }


    return render(request, 'AppTravel/vuelos.html',contexto)

#creacion de formulario para la parte de reserva de hotel 
def reserva_hotel(request):

    if request.method == 'POST':
        mi_formulario = ReservaHotel(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            hotel1 = Hotel(nombreH=data.get('nombreH'), num_personas=data.get('num_personas'), dia_entrada=data.get('dia_entrada'), dia_salida=data.get('dia_salida'))
            hotel1.save()

            return redirect('AppTravelReservaHotel')
   
    contexto = {
        'form': ReservaHotel()
    }


    return render(request, 'AppTravel/reserva_hotel.html',contexto)

# busqueda en progreso, no se porque no funciona...
def busqueda_post(request):
    email = request.GET.get('email')


    usuarios = Usuario.objects.filter(email__icontains=email)
    contexto = {
        'usuarios': usuarios,
    }
    return render(request, 'AppTravel/filtro.html', contexto)



def busqueda(request):
    
    contexto = {
        'formusu': BusquedaUsuarios(),

    }

    return render(request, 'AppTravel/busqueda.html',contexto)




