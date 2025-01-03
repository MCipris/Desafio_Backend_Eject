from apps.mini_twitter.models import Postagem, Comentario, Like
from apps.mini_twitter.serializers import PostagemSerializer, ComentarioSerializer
from rest_framework import viewsets

# Create your views here.
class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

