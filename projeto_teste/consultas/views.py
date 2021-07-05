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

from garagem.models import Garagem
from garagem.serializers import GaragemSerializer, GaragemOnlySerializer







class ConsultaClientesViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class =  PessoaSerializer

class ConsultaGaragensViewSet(viewsets.ModelViewSet):
    queryset = Garagem.objects.all()
    serializer_class =  GaragemOnlySerializer

class ConsultaClientesGaragemSemVeiculosViewSet(viewsets.ModelViewSet):
    queryset = Garagem.objects.all()
    serializer_class =  GaragemSerializer

api_view(['GET'])
def consultaClientesGaragemVeiculosView(request):
    dicDados= {}
    idGaragens = []
    listVeiculos = []
    garagem = Garagem.objects.all()
    print(garagem)
    garagem = garagem.filter().extra(select={
                                      "veiculo":
                                      " SELECT descricao FROM veiculo WHERE garagem = "
                                      " id ",
                                     }).values('id','pessoa', 'descricao', 'veiculo')
    for i in garagem:
        if i['veiculo'] != None:
           idGaragens.append(i['id'])
           listVeiculos.append('veiculo: ' + str(i['veiculo']) - ' garagem: ' + str(i['descricao']) )
    print(garagem)
    garagem = garagem.filter(id__in=idGaragens)
    print(listVeiculos)

    garagemJson = serializers.serialize("json",garagem)
    garagemObj = json.loads(garagemJson)

    return HttpResponse(json.dumps(garagemObj), content_type='application/json')



api_view(['GET'])
def consultaClientesGaragemSVeiculosView(request):
    dicDados= {}
    idGaragens = []
    listVeiculos = []
    garagem = Garagem.objects.all()
    garagens = garagem.filter().extra(select={
                                      "veiculo":
                                      " SELECT descricao FROM veiculo WHERE garagem = "
                                      " id ",
                                     }).values('id','pessoa', 'descricao', 'veiculo')
    for i in garagens:
        if i['veiculo'] == None:
           idGaragens.append(i['id'])


    garagem = garagem.filter(id__in=idGaragens)


    print(garagem)
    garagemJson = serializers.serialize("json",garagem)
    garagemObj = json.loads(garagemJson)

    return HttpResponse(json.dumps(garagemObj),  content_type='application/json')





'''
Por fim crie uma API para uma aplicação terceira consultar todos os clientes
cadastrados, todas as garagens ativas, e quais clientes possuem veículos
vinculados a suas garagens e quais não possue
'''
