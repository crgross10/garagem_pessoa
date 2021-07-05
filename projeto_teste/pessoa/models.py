from django.db import models
from projeto_teste import choices
# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200,  unique=True)
    tipo = models.IntegerField(choices=choices.TIPO_PESSOA_CHOICES, default=1)

    class Meta:
        ordering = ['nome']
        db_table = 'pessoa'

    def __str__(self):
        return self.nome
