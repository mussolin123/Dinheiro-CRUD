# user/urls.py
from django.urls import path
from .views import RegisterUserView, LoginUserView, UserProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),  # Cadastro de Usuário
    path('login/', LoginUserView.as_view(), name='login'),  # Login de Usuário
    path('profile/', UserProfileView.as_view(), name='profile'),  # Perfil de Usuário
]
