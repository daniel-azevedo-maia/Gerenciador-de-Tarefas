from django.contrib import admin
from tarefas.models import Tarefa, Pessoa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'situacao', 'criacao')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_filter = ('situacao',)
    list_per_page = 20

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'sobrenome', 'email')
    list_per_page = 20
