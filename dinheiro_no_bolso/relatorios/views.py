from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db import models
from .models import Relatorio
from .models import Despesa
from django.db.models import Sum

class RelatorioView(APIView):
    # Requer autenticação para acessar o relatório
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        relatorio = Relatorio()

        # Exemplo de resumo de despesas pagas e pendentes
        total_pago = relatorio.total_por_status(True)
        total_pendente = relatorio.total_por_status(False)
        
        # Resumo de despesas por tipo
        tipos = ['Água', 'Luz', 'Aluguel', 'Mercado', 'Farmácia', 'Lazer']
        total_por_tipo = {tipo: relatorio.total_por_tipo(tipo) for tipo in tipos}
        
        # Relatório mensal (exemplo de janeiro de 2024)
        total_mensal = relatorio.total_mensal(1, 2024)

        return Response({
            'total_pago': total_pago,
            'total_pendente': total_pendente,
            'total_por_tipo': total_por_tipo,
            'total_mensal': total_mensal
        })

class RelatorioCategoriaView(APIView):
    # Permite acesso sem autenticação
    permission_classes = [AllowAny]

    def get(self, request):
        # Lógica para gerar o relatório de despesas por categoria
        categorias = Despesa.objects.values('categoria').annotate(total=models.Sum('valor'))
        return Response(categorias)
