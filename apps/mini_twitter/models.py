from django.db import models
from django.contrib.auth.models import User

class Postagem(models.Model):
    descricao = models.CharField(max_length = 280, blank = False, null = False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

class Comentario(models.Model):
    descricao = models.CharField(max_length = 280, blank = False, null = False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        to=Postagem,
        on_delete=models.CASCADE
    )

class Like(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    post = models.ForeignKey(Postagem, models.CASCADE)