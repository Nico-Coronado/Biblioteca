from django.db import models

from libro.models import Libro
from users.models import User


class Prestamo(models.Model):
    # ForeignKey para el user de la aplicacion users
    lector = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo =  models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    def save(self, *args, **kwargs):
        self.libro.stock = self.libro.stock - 1
        self.libro.save()   # Cada vez que se haga un registro se restara 1
                            # al stock de la tabla Libro(incluye el admin)
    def __str__(self):
        return self.libro.titulo
