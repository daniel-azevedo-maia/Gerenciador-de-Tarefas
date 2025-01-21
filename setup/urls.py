from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from tarefas.views import TarefaViewSet, PessoaViewSet

router = routers.DefaultRouter()
router.register('tarefas', TarefaViewSet, basename='Tarefas')
router.register('pessoas', PessoaViewSet, basename='Pessoas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API REST
    path('', TemplateView.as_view(template_name='index.html')),  # Front-End
]
