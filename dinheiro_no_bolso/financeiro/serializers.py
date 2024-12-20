from rest_framework import serializers
from .models import Salario

class SalarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salario
        fields = ['valor']
