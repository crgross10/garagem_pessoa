from rest_framework import serializers
from .models import Garagem, Veiculo


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Veiculo
        fields=('__all__')

class GaragemSerializer(serializers.ModelSerializer):
    veiculos = VeiculoSerializer(many=True,read_only=True)
    class Meta:
        model= Garagem
        fields=('id','descricao','pessoa', 'veiculos')


class GaragemOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model= Garagem
        fields=('__all__')
