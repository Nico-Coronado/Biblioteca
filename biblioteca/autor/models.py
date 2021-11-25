from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    # Si el numero obligatoriamente debe ser positivo debemos colocar
    # PositiveIntegerField() para las validaciones por parte de django
    edad = models.PositiveIntegerField(default=0)    

    def __str__(self):
        return self.nombre
