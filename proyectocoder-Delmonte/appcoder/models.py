from django.db import models

# Create your models here.


class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    bioma = models.CharField(max_length=50)


class Vertebrado(models.Model):
    nombre = models.CharField(max_length=50)
    bioma = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)


class Invertebrado(models.Model):
    nombre = models.CharField(max_length=50)
    bioma = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    


