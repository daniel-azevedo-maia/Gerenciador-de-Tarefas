from django.db import models

class Pessoa(models.Model):

    nome = models.CharField(max_length = 200, verbose_name="Nome")
    sobrenome = models.CharField(max_length = 200, verbose_name="Sobrenome")
    email = models.EmailField(unique=True, verbose_name="Email")

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    

class Tarefa(models.Model):

    SITUACAO = (
        ('P', 'PENDENTE'),
        ('C', 'CONCLUÍDA'),
        ('A', 'ATRASADA'),
        ('X', 'PRÓXIMA DE EXPIRAR')
    )

    titulo = models.CharField(max_length = 200, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    prazo_para_conclusao = models.DateTimeField(verbose_name="Prazo para conclusão")
    situacao = models.CharField(max_length=1, choices=SITUACAO, blank=False, default='P')
    pessoa = models.ForeignKey(Pessoa, related_name="pessoas", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo