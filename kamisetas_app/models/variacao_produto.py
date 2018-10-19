# coding: utf-8
from django.db import models
from django.core.validators import MinValueValidator

class VariacaoProduto(models.Model):
    descricao = models.CharField(max_length=200)
    preco = models.IntegerField(validators=[MinValueValidator(0)])
    qtd_estoque = models.IntegerField(validators=[MinValueValidator(0)])

    def __unicode__(self):
        return '%s' % self.id

    def __str__(self):
        return '%s' % self.id