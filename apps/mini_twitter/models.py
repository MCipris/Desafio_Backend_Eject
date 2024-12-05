from django.db import models

class Postagem(models.Model):
    descricao = models.TextField(blank = False, null = False)