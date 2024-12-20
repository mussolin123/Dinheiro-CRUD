from django.db import models

class Salario(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Salário: {self.valor}"
