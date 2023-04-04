
from django.contrib import admin
from django.urls import path, include
from tarefas.views import PessoaViewSet, TarefaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tarefas', TarefaViewSet, basename='Tarefas')
router.register('pessoas', PessoaViewSet, basename='Pessoas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
