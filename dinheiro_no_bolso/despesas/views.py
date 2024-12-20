from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Despesa
from .serializers import DespesaSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all().order_by('-data')
    serializer_class = DespesaSerializer

    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def resumo(self, request):
        """
        Ação de resumo para visualizar os totais das despesas pagas e pendentes.
        Não exige autenticação.
        """
        total_pago = Despesa.objects.filter(status_pago=True).aggregate(Sum('valor'))['valor__sum'] or 0
        total_pendente = Despesa.objects.filter(status_pago=False).aggregate(Sum('valor'))['valor__sum'] or 0

        return Response({
            'total_pagas': total_pago,
            'total_pendentes': total_pendente
        })
