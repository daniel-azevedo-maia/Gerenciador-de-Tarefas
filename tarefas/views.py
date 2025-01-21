from django.shortcuts import render
from rest_framework import viewsets
from tarefas.models import Tarefa, Pessoa
from .serializer import TarefasSerializer, PessoaSerializer
from django.views.generic import TemplateView

class TarefaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as tarefas"""
    queryset = Tarefa.objects.all().order_by('-criacao')
    serializer_class = TarefasSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as pessoas"""
    queryset = Pessoa.objects.all().order_by('nome')
    serializer_class = PessoaSerializer

class FrontendAppView(TemplateView):
    """Renderiza o front-end"""
    template_name = "index.html"
