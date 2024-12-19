from django.db import models
from despesas.models import Despesa  # Importando o modelo Despesa do app 'despesas'

class Relatorio(models.Model):
    data_geracao = models.DateTimeField(auto_now_add=True)

    def total_por_status(self, status_pago):
        """Retorna o total de despesas baseado no status pago"""
        total = Despesa.objects.filter(status_pago=status_pago).aggregate(models.Sum('valor'))['valor__sum'] or 0
        return total

    def total_por_tipo(self, tipo):
        """Retorna o total de despesas baseado no tipo"""
        total = Despesa.objects.filter(tipo=tipo).aggregate(models.Sum('valor'))['valor__sum'] or 0
        return total

    def total_mensal(self, mes, ano):
        """Retorna o total de despesas de um mês específico"""
        total = Despesa.objects.filter(data__month=mes, data__year=ano).aggregate(models.Sum('valor'))['valor__sum'] or 0
        return total

    def total_ano(self, ano):
        """Retorna o total de despesas de um ano específico"""
        total = Despesa.objects.filter(data__year=ano).aggregate(models.Sum('valor'))['valor__sum'] or 0
        return total
