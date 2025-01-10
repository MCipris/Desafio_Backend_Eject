from rest_framework import serializers
from .models import Postagem, Comentario, Curtida
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        ) 
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = ['descricao', 'data_criacao']
        read_only_fields = ['usuario']

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['descricao', 'data_criacao', 'postagem']
        read_only_fields = ['usuario']

class CurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curtida
        fields = '__all__'