from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DespesaViewSet

# Configurando o roteamento das APIs
router = DefaultRouter()
router.register(r'despesas', DespesaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
