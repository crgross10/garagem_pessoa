from django.db import models
from projeto_teste import choices
from pessoa.models import Pessoa


class Garagem(models.Model):
    descricao = models.CharField(max_length=200)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name = 'pessoas',  db_column='pessoa')

    class Meta:
        ordering = ['descricao']
        db_table = 'garagem'

    def __str__(self):
        return self.descricao


class Veiculo(models.Model):
    descricao = models.CharField(max_length=200)
    cor =  models.CharField(max_length=20)
    ano =  models.IntegerField()
    modelo = models.CharField(max_length=50)
    tipo = models.IntegerField(choices=choices.TIPO_VEICULO_CHOICES)
    garagem = models.ForeignKey(Garagem, on_delete=models.CASCADE, related_name = 'veiculos',  db_column='garagem', null=True)
    class Meta:
        ordering = ['descricao']
        db_table = 'veiculo'

    def __str__(self):
        return self.descricao
