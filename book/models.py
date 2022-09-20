from django.db import models
from datetime import date


class Books(models.Model):
    nome = models.CharField(max_length=128)
    autor = models.CharField(max_length=64)
    co_autor = models.CharField(max_length=64, blank=True)
    data_cadastro = models.DateField(default=date.today())
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=64, blank=True, null=True)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Book'

    def __str__(self):
        return self.nome
