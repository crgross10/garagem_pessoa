from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.response import Response
import json
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

from pessoa.models import Pessoa
from pessoa.serializers import PessoaSerializer

from garagem.models import Garagem, Veiculo
from garagem.serializers import GaragemSerializer, GaragemOnlySerializer




class ConsultaClientesViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class =  PessoaSerializer

class ConsultaGaragensViewSet(viewsets.ModelViewSet):
    queryset = Garagem.objects.all()
    serializer_class =  GaragemOnlySerializer


api_view(['GET'])
def consultaClientesGaragemVeiculosView(request):
    dicDados= {}
    idGaragens = []
    listVeiculos = []

    pessoa = Pessoa.objects.all()
    garagem = Garagem.objects.all()
    veiculo =  Veiculo.objects.all()
    count=0

    for p in pessoa:
        dicVeiculos= {}
        countVeic = 0
        count=count+1
        gar = garagem.filter(pessoa=p)
        for g in gar:
            veic =  veiculo.filter(garagem=g)
            if len(veic) > 0:
                for v in veic:
                    print(countVeic)
                    countVeic= countVeic+1
                    dicVeiculos.update({countVeic:{'descricao': v.descricao, 'cor': v.cor, 'ano': v.ano, 'modelo': v.modelo}})

            if len(dicVeiculos) > 0:
                dicDados.update({'Ciente'+ str(count) :{'nome':p.nome, 'telefone': p.telefone, 'e-mail':p.email, 'Garagem':{'descricao': g.descricao, 'veiculos':dicVeiculos}}})

    return HttpResponse(json.dumps(dicDados), content_type='application/json')



api_view(['GET'])
def consultaClientesGaragemSVeiculosView(request):
    dicDados= {}
    idGaragens = []
    listVeiculos = []

    pessoa = Pessoa.objects.all()
    garagem = Garagem.objects.all()
    veiculo =  Veiculo.objects.all()
    count=0
    for p in pessoa:
        count=count+1
        gar = garagem.filter(pessoa=p)
        for g in gar:
            veic =  veiculo.filter(garagem=g)
            if len(veic) == 0:
                dicDados.update({'Ciente'+ str(count) :{'nome':p.nome, 'telefone': p.telefone, 'e-mail':p.email, 'Garagem':{'descricao': g.descricao}}})

    return HttpResponse(json.dumps(dicDados),  content_type='application/json')






'''
Por fim crie uma API para uma aplicação terceira consultar todos os clientes
cadastrados, todas as garagens ativas, e quais clientes possuem veículos
vinculados a suas garagens e quais não possue
'''
