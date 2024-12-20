from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        app_label = 'categorias'
