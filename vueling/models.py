from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    aeropuerto = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

class Pasajero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    tipo_identificacion = models.CharField(max_length=3)
    numero_documento = models.IntegerField()
    # vuelos = models.ManyToManyField(Ciudad,blank=True, null=True)
