from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db import models
from .models import Relatorio
from .models import Despesa

class RelatorioView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        relatorio = Relatorio()

        total_pago = relatorio.total_por_status(True)
        total_pendente = relatorio.total_por_status(False)
        
        tipos = ['Água', 'Luz', 'Aluguel', 'Mercado', 'Farmácia', 'Lazer']
        total_por_tipo = {tipo: relatorio.total_por_tipo(tipo) for tipo in tipos}
        
        total_mensal = relatorio.total_mensal(1, 2024)

        return Response({
            'total_pago': total_pago,
            'total_pendente': total_pendente,
            'total_por_tipo': total_por_tipo,
            'total_mensal': total_mensal
        })

class RelatorioCategoriaView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categorias = Despesa.objects.values('categoria').annotate(total=models.Sum('valor'))
        return Response(categorias)
