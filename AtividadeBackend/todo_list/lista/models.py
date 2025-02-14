from django.db import models

# Create your models here.
class Tarefa(models.Model):
    descricao = models.CharField(max_length=255)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao