from django.db import models
from django.db.models.fields import PositiveIntegerField

from autor.models import Autor


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)


    def __str__(self):
        return self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo =  models.CharField(max_length=50)
    fecha = models.DateField("Fecha de lanzamiento")
    portada = models.ImageField("Imagen de portada", upload_to="portadas")
    visitas = models.PositiveIntegerField()
    stock = PositiveIntegerField(default=0)
    # class Meta:
        # La clase meta nos ayudara a personalizar el administrador de django

    def __str__(self):
        return str(self.categoria.id) + ' ' + self.titulo