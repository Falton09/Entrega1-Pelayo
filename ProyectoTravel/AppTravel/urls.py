from django.urls import path

from AppTravel.views import *

urlpatterns = [
    path('', inicio, name='AppTravelInicio'),

]