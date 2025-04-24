from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAbs(AbstractUser):
    telefone = models.PositiveIntegerField(blank=True, null=True)
    cargo = models.CharField(max_length=30, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    idade = models.PositiveIntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    escolaridade = models.CharField(max_length=50, blank=True, null=True)
    animais = models.PositiveIntegerField(blank=True, null=True)  

    def __str__(self):
        return self.username
