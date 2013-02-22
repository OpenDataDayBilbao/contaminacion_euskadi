# coding: utf-8

from django.db import models

# Create your models here.

#########################
# Model: AirPollution
#########################


class AirPollution(models.Model):
    ejercicio = models.IntegerField()
    nif = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    nima = models.IntegerField()
    denominacion = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    contaminante = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    cod_prtr = models.IntegerField()
    cantidad_kg_aino = models.FloatField()
