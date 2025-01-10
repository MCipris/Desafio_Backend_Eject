from django.db import models
from django.contrib.auth.models import User

class Postagem(models.Model):
    descricao = models.CharField(max_length = 280, blank = False, null = False)
    data_criacao = models.DateTimeField(auto_now_add=True, blank = False, null = False)
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE, blank = False, null = False)

    def __str__(self):
        return 'id: '+str(self.id)+' user: '+self.usuario.username

class Comentario(models.Model):
    descricao = models.CharField(max_length = 280, blank = False, null = False)
    data_criacao = models.DateTimeField(auto_now_add=True, blank = False, null = False)
    postagem = models.ForeignKey(to=Postagem, on_delete=models.CASCADE, blank = False, null = False)
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE, blank = False, null = False)

class Curtida(models.Model):
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE, blank = False, null = False)
    postagem = models.ForeignKey(to=Postagem, on_delete=models.CASCADE, blank = False, null = False)

    def __str__(self):
        return self.usuario.username