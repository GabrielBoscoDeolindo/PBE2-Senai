from django.db import models

from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=35)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo
