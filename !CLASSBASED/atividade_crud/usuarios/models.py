from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    biografia = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=30)
    endereco = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=100)
    animais = models.IntegerField()

    def __str__(self):
        return self.nome
