from django.urls import path
from .views import SalarioView, PrevisaoView

urlpatterns = [
    path('salario/', SalarioView.as_view(), name='salario'),
    path('previsao/', PrevisaoView.as_view(), name='previsao'),
]
