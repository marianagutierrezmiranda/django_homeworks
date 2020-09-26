from django.db import models


class Productos(models.Model):
    nombre = models.CharField(max_length=100)


class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
