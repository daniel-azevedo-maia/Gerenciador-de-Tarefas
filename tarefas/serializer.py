from rest_framework import serializers
from tarefas.models import Tarefa, Pessoa

class TarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'descricao', 'criacao', 'prazo_para_conclusao', 'situacao', 'pessoa']


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'