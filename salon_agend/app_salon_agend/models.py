from django.db import models

# Create your models here.
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    duracao = models.DurationField()

class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    data = models.DateField()
    hora = models.TimeField()
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='servicos')
    profissional = models.CharField(max_length=100)
    