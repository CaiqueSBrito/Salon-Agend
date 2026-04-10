from django.db import models

# Create your models here.

class Calendario(models.Model):
    data = models.DateField()
    horario = models.TimeField()

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField(default=60, blank=True, null=True)

class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    data = models.DateField()
    hora = models.TimeField()
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='agendamentos')
    profissional = models.CharField(max_length=100, default='Profissional 1')

class DiaBloqueado(models.Model):
    data = models.DateField(unique=True)
    motivo = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Bloqueio: {self.data}"
    