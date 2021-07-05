from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pessoa
from garagem.models import Garagem
from garagem.serializers import GaragemSerializer
from .serializers import PessoaSerializer

# Create your views here.
class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class =  PessoaSerializer

    @action(detail=False, methods=['POST'])
    def cadastrarPessoaGaragem(self, request, pk = None):
        serializer_pessoa = PessoaSerializer(data = request.data)
        serializer_pessoa.is_valid(raise_exception=True)
        serializer_pessoa.save()

        serializer_garagem =  GaragemSerializer(data={'descricao': 'Garagem do ' + str(serializer_pessoa.data['nome']), 'pessoa': serializer_pessoa.data['id']})
        serializer_garagem.is_valid(raise_exception=True)
        serializer_garagem.save()

        return Response({"msg":"Salvo com sucesso!"})
