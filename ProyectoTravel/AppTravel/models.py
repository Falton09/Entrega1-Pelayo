from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

class Vuelos(models.Model):
    destino = models.CharField(max_length=40)
    fecha_salida = models.DateField()
    fecha_regreso = models.DateField()
    num_personas = models.IntegerField()

class Hotel(models.Model):
    nombreH = models.CharField(max_length=40)
    num_personas = models.IntegerField()
    dia_entrada = models.DateField()
    dia_salida = models.DateField()


   
