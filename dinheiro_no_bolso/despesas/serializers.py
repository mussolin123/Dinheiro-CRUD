from rest_framework import serializers
from .models import Despesa

# Serializer para a Despesa
class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = ['id', 'descricao', 'tipo', 'data', 'valor', 'status_pago']