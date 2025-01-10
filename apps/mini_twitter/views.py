from apps.mini_twitter.models import Postagem, Comentario, Curtida
from apps.mini_twitter.serializers import UserSerializer, PostagemSerializer, ComentarioSerializer, CurtidaSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Endpoint para CRUD de usuários.
    
    Métodos HTTP Permitidos: 
    - GET /users/ -> Lista todos os usuários por ordem de data de criação.
    - GET /users/{id}/ -> Retorna um usuários em específico.
    - POST /users/ -> Cria um novo usuário.
    - PUT /users/{id}/ -> Atualiza um usuário existente.
    - DELETE /users/{id}/ -> Remove um usuário existente.

    Classe de serializer:
    - UserSerializer: usado para serialização e desserialização de dados.
    
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostagemViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Endpoint para CRUD de postagens.
    
    Métodos HTTP Permitidos: 
    - GET /postagens/ -> Lista todas as postagens por ordem de data de criação.
    - GET /postagens/{id}/ -> Retorna uma postagem em específico.
    - POST /postagens/ -> Cria uma nova postagem.
    - PUT /postagens/{id}/ -> Permite atualizar uma postagem existente completamente.
    - PATCH /postagens/{id}/ -> Permite atualizar uma postagem existente parcialmente.
    - DELETE /postagens/{id}/ -> Remove uma postagem existente.

    Classe de serializer:
    - PostagemSerializer: usado para serialização e desserialização de dados.
    
    """
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Postagem.objects.all().order_by('-data_criacao')
    serializer_class = PostagemSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)        

class ComentarioViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Endpoint para CRUD de comentários.
    
    Métodos HTTP Permitidos: 
    - GET /comentarios/ -> Lista todos os comentários por ordem de data de criação.
    - GET /comentarios/{id}/ -> Retorna um comentário em específico.
    - POST /comentarios/ -> Cria um novo comentário.
    - PUT /comentarios/{id}/ -> Atualiza um comentário existente.
    - DELETE /comentarios/{id}/ -> Remove um comentário existente.

    Classe de serializer:
    - ComentarioSerializer: usado para serialização e desserialização de dados.
    
    """
    authentication_class = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class CurtidaViewSet(viewsets.ModelViewSet):
    """
    Descrição da View:
    - Endpoint para CRUD de curtidas.
    
    Métodos HTTP Permitidos: 
    - GET /curtidas/ -> Lista todas as curtidas por ordem de data de criação.
    - GET /curtidas/{id}/ -> Retorna uma curtida em específico.
    - POST /curtidas/ -> Cria uma nova curtida.
    - PUT /curtidas/{id}/ -> Permite atualizar uma curtida existente completamente.
    - PATCH /curtidas/{id}/ -> Permite atualizar uma curtida existente parcialmente.
    - DELETE /curtidas/{id}/ -> Remove uma curtida existente.

    Classe de serializer:
    - CurtidaSerializer: usado para serialização e desserialização de dados.
    
    """

    authentication_class = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Curtida.objects.all()
    serializer_class = CurtidaSerializer