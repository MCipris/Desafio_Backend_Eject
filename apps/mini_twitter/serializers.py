from rest_framework import serializers
from .models import Postagem, Comentario, Curtida
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class CurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curtida
        fields = '__all__'