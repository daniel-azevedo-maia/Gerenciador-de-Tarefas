from django.contrib import admin
from tarefas.models import Tarefa, Pessoa

class Tarefas(admin.ModelAdmin):
    
    list_display = ('id', 'titulo', 'situacao')

    list_display_links = ('id', 'titulo')

    search_fields = ('titulo', )

    list_per_page = 20

admin.site.register(Tarefa, Tarefas)

class Pessoas(admin.ModelAdmin):

    list_display = ('id', 'nome', 'sobrenome')

    list_display_links = ('id', 'nome')

    search_fields = ('nome', 'sobrenome', )

    list_per_page = 20

admin.site.register(Pessoa, Pessoas)