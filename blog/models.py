from django.db import models

class ListaDeDistribucion(models.Model):
    email = models.CharField(max_length=100)