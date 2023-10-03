from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    numero = models.IntegerField()

class Entrenador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()

class Logro(models.Model):
    nombre = models.CharField(max_length=20)
    ano = models.IntegerField()
