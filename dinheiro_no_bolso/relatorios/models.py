from django.db import models
from despesas.models import Despesa

class Relatorio(models.Model):
    data_geracao = models.DateTimeField(auto_now_add=True)

#Retorna o total de despesas baseado nos tatus
    def total_por_status(self, status_pago):
        
        total = Despesa.objects.filter(status_pago=status_pago).aggregate(models.Sum('valor'))['valor__sum'] or 0
        return total

    def total_por_tipo(self, tipo):
        total = Despesa.objects.filter(tipo=tipo).aggregate(models.Sum('valor'))['valor__sum'] or 0
        return total

    def total_mensal(self, mes, ano):
        total = Despesa.objects.filter(data__month=mes, data__year=ano).aggregate(models.Sum('valor'))['valor__sum'] or 0
        return total

    def total_ano(self, ano):
        total = Despesa.objects.filter(data__year=ano).aggregate(models.Sum('valor'))['valor__sum'] or 0
        return total
