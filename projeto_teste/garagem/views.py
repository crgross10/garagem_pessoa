from django.shortcuts import render
from rest_framework import viewsets
from .models import Garagem, Veiculo
from .serializers import GaragemSerializer, VeiculoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import json
from django.http import HttpResponse

# Create your views here.
class GaragemViewSet(viewsets.ModelViewSet):
    queryset = Garagem.objects.all()
    serializer_class =  GaragemSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.filter(garagem=None)
    serializer_class =  VeiculoSerializer

    @action(detail=True, methods=['get'])
    def retornaDadosVeiculo(self, request, pk=None):
        dicDados = {}
        veiculo = Veiculo.objects.filter(pk=pk)
        print(veiculo)
        for i in veiculo:
            if i.tipo == 1:
                dicDados.update({'cor': i.cor, 'ano':i.ano})
            else:
                dicDados.update({'modelo': i.modelo, 'ano':i.ano})

        return  HttpResponse(json.dumps(dicDados), content_type='application/json')
