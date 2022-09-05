from django.urls import path

from AppTravel.views import *

urlpatterns = [
    path('', inicio, name='AppTravelInicio'),
    path('vuelos/',vuelo, name='AppTravelVuelos'),
    path('Reservahotel/',reserva_hotel, name='AppTravelReservaHotel'),

]