from django.contrib import admin
from .models import Postagem, Comentario

# Register your models here.
class Postagens(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', 'descricao',)
    search_fields = ('descricao',)

admin.site.register(Postagem, Postagens)

class Comentarios(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', 'descricao',)
    list_per_page = 20
    search_fields = ('descricao',)

admin.site.register(Comentario, Comentarios)