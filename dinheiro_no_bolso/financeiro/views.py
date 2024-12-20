from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Salario

class SalarioView(APIView):
    def post(self, request):
        salario_data = request.data.get('valor')
        if not salario_data:
            return Response({"error": "O campo 'valor' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        # Salva o salário
        salario = Salario.objects.create(valor=salario_data)

        return Response({"message": "Salário salvo com sucesso.", "valor": salario.valor}, status=status.HTTP_200_OK)

class PrevisaoView(APIView):
    def post(self, request):
        salario_data = request.data.get('valor')
        if not salario_data:
            return Response({"error": "O campo 'valor' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        # Calcula a regra 50/30/20 com base no valor fornecido
        salario = float(salario_data)
        needs = salario * 0.50
        wants = salario * 0.30
        savings = salario * 0.20

        return Response({
            "salario": salario,
            "budget": {
                "necessidades": needs,
                "desejos": wants,
                "economias": savings
            }
        })
