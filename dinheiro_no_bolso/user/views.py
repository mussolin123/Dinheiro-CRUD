from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from .serializers import RegisterUserSerializer, LoginUserSerializer
from rest_framework import status
from django.contrib.auth import authenticate

# View para o Cadastro de Usuário
class RegisterUserView(APIView):
    permission_classes = [AllowAny]  # Permite o acesso público

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Gerar o token JWT (somente access token)
            access_token = str(AccessToken.for_user(user))

            return Response({
                'username': user.username,
                'email': user.email,
                'access_token': access_token
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View para o Login de Usuário (Autenticação)
class LoginUserView(APIView):
    permission_classes = [AllowAny]  # Permite o acesso público

    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            # Verifica as credenciais
            user = authenticate(username=username, password=password)
            if user is not None:
                # Gerar o token JWT (somente access token)
                access_token = str(AccessToken.for_user(user))
                return Response({
                    'access_token': access_token
                }, status=status.HTTP_200_OK)
            return Response({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View para obter o perfil do usuário autenticado
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Requer autenticação

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
        })
