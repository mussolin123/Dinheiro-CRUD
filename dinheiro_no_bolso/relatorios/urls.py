from django.urls import path
from .views import RelatorioView, RelatorioCategoriaView

urlpatterns = [
    path('', RelatorioView.as_view(), name='relatorios'),
    path('categoria/', RelatorioCategoriaView.as_view(), name='relatorio-categoria'),
]
