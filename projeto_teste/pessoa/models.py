from django.db import models
from projeto_teste import choices
from django.contrib.auth import get_user_model
# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200,  unique=True)
    tipo = models.IntegerField(choices=choices.TIPO_PESSOA_CHOICES, default=1)
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_column='id_user', blank=True, null=True)
    class Meta:
        ordering = ['nome']
        db_table = 'pessoa'

    def __str__(self):
        return self.nome
