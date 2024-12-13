from django.db import models

class Postagem(models.Model):
    descricao = models.CharField(max_length = 280, blank = False, null = False)
    data_criacao = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    descricao = models.CharField(max_length = 280, blank = False, null = False)
    data_criacao = models.DateTimeField(auto_now_add=True)