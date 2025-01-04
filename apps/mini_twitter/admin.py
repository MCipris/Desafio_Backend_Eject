from django.contrib import admin
from .models import Postagem, Comentario, Curtida
from django.contrib.auth.models import User

# Register your models here.
class Users(admin.ModelAdmin):
    list_display = ('id', 'username',)
    list_display_links = ('id', 'username',)
    list_per_page = 10
    search_fields = ('username',)

class Postagens(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', 'descricao',)
    list_per_page = 10
    search_fields = ('descricao',)

admin.site.register(Postagem, Postagens)

class Comentarios(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', 'descricao',)
    list_per_page = 10
    search_fields = ('descricao',)

admin.site.register(Comentario, Comentarios)

class Curtidas(admin.ModelAdmin):
    list_display = ('id', 'user',)
    list_display_links = ('id', 'user',)
    list_per_page = 10

admin.site.register(Curtida, Curtidas)