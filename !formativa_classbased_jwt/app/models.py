from django.db import models


# Create your models here.
PERIODO_CHOICES = [
    ('manha', 'manha'),
    ('tarde', 'tarde'),
    ('noite', 'noite'),
]

class Professor(models.Model):
    ni = models.CharField(max_length=20, unique=True)  
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField()
    
    class Meta:
        verbose_name_plural = "Professor"

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()
    descricao = models.TextField()
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='disciplinas_responsaveis')

    class Meta:
        verbose_name_plural = "Disciplina"

    def __str__(self):
        return self.nome

class ReservaAmbiente(models.Model):
    data_inicio = models.DateField()
    data_termino = models.DateField()
    periodo = models.CharField(max_length=6, choices=PERIODO_CHOICES)
    sala_reservada = models.CharField(max_length=50)
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='reservas')
    disciplina_associada = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f"Reserva de {self.sala_reservada} - {self.data_inicio} a {self.data_termino}"
