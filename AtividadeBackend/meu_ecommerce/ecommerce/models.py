from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='images/', null=True) 

    def __str__(self):
        return self.nome
