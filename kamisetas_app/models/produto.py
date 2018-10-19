# coding: utf-8
from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=200)
    marca = models.CharField(max_length=200, null=True, blank=True)
    variacao = models.ForeignKey('kamisetas_app.VariacaoProduto', related_name='produto_variacao', on_delete=models.CASCADE)
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.descricao

    def __str__(self):
        return '%s' % self.descricao