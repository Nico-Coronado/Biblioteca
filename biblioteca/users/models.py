from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from . managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otros")
    )

    username = models.CharField("Username", max_length=50, unique=True)
    email = models.EmailField()
    nombres = models.CharField("Nombres", max_length=30, blank=True)
    apellidos = models.CharField("Apellidos", max_length=30, blank=True)
    genero = models.CharField("Genero", max_length=1, choices=GENDER_CHOICES, blank=True)
    # Nos pide que definamos la variable desde AbstractBaseUser el USERNAME_FIELD
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username' 

    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos' 'genero',]

    objects = UserManager()

    def __str__(self):
        return self.username
