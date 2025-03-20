from django.db import models

# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=250)
    data = models.DateField()
    local = models.CharField(blank=True, max_length=50)
    categoria = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.nome
    
    