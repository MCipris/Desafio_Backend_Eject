from apps.mini_twitter.models import Postagem, Comentario, Curtida
from apps.mini_twitter.serializers import UserSerializer, PostagemSerializer, ComentarioSerializer, CurtidaSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all().order_by('-data_criacao')
    serializer_class = PostagemSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class CurtidaViewSet(viewsets.ModelViewSet):
    queryset = Curtida.objects.all()
    serializer_class = CurtidaSerializer