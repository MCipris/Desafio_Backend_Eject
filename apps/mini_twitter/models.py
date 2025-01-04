from django.db import models
from django.contrib.auth.models import User

class Postagem(models.Model):
    descricao = models.CharField(max_length = 280, blank = False, null = False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return 'id: '+str(self.id)+' user: '+self.usuario.username

class Comentario(models.Model):
    descricao = models.CharField(max_length = 280, blank = False, null = False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(to=Postagem, on_delete=models.CASCADE)

class Curtida(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Postagem, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+' '+self.user.username