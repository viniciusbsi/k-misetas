# coding: utf-8
from django.db import models

class CarrinhoUser(models.Model):
    produto = models.ForeignKey('Produto', related_name='Carrinho_produto')

    def __unicode__(self):
        return '%s' % self.id

    def __str__(self):
        return '%s' % self.id