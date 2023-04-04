from django.shortcuts import render
from rest_framework import viewsets
from tarefas.models import Tarefa, Pessoa
from .serializer import TarefasSerializer, PessoaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as tarefas"""
    queryset = Tarefa.objects.all()
    serializer_class = TarefasSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as tarefas"""
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer