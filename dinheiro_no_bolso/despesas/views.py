from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Despesa
from .serializers import DespesaSerializer

# ViewSet CRUD das Despesas
class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all().order_by('-data')
    serializer_class = DespesaSerializer

    # Soma das despesas pagas e não pagas
    @action(detail=False, methods=['get'])
    def resumo(self, request):
        total_pago = Despesa.objects.filter(status_pago=True).aggregate(models.Sum('valor'))['valor__sum'] or 0
        total_pendente = Despesa.objects.filter(status_pago=False).aggregate(models.Sum('valor'))['valor__sum'] or 0
        return Response({
            'total_pagas': total_pago,
            'total_pendentes': total_pendente
        })
