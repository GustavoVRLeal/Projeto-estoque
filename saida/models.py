from django.db import models
from produto.models import Produtos

class Saidas(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.IntegerField('Quantidade', default=0)
    preco = models.FloatField('Preço', default=0)