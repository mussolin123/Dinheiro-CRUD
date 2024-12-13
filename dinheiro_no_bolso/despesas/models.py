from django.db import models

# Modelo de Despesa
class Despesa(models.Model):
    TIPO_DESPESA = [
        ('Água', 'Água'),
        ('Luz', 'Luz'),
        ('Aluguel', 'Aluguel'),
        ('IPVA', 'IPVA'),
        ('IPTU', 'IPTU'),
        ('Mercado', 'Mercado'),
        ('Farmácia', 'Farmácia'),
        ('Lazer', 'Lazer'),
        ('Esportes', 'Esportes'),
        ('Contas Diversas', 'Contas Diversas'),
    ]

    descricao = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_DESPESA)
    data = models.DateField(auto_now_add=True)
    valor = models.FloatField()
    status_pago = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.descricao} - {self.tipo} - R${self.valor}'
