from django.db import models
from django.db.models.fields import PositiveIntegerField
from django.db.models.signals import post_save
# 
from PIL import Image

from autor.models import Author
from . managers import BookManager

class Category(models.Model):
    category = models.CharField("Categoria", max_length=50)

    def __str__(self):
        return self.category

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categoria_libro')
    authors = models.ManyToManyField(Author)
    title =  models.CharField(max_length=50)
    description = models.TextField(max_length=150,)
    date = models.DateField("Fecha de lanzamiento")
    cover_page = models.ImageField("Imagen de portada", upload_to="portadas")
    visits = models.PositiveIntegerField()
    stock = PositiveIntegerField(default=0)

    objects = BookManager()

    def __str__(self):
        return self.title

# lower the quality of the cover by 20%
def optimizeImage(sender,instance, **kwargs):
    if instance.cover_page:
        portada = Image.open(instance.cover_page.path) 
        portada.save(instance.cover_page.path, quality=20, optimize=True) 
                                                                       
post_save.connect(optimizeImage, sender=Book)