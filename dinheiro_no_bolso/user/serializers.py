# user/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

# Serializer para o Cadastro do Usuário
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
    def create(self, validated_data):
        # Cria um usuário com senha criptografada
        user = User.objects.create_user(**validated_data)
        return user

# Serializer para a Autenticação do Usuário
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
