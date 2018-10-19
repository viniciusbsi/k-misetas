# coding: utf-8
from django.db import models
from django.core.validators import MinValueValidator
from kamisetas_app.models import FormaPagamento
from kamisetas_app.models import CarrinhoUser


class Pedido(models.Model):
    carrinho = models.ForeignKey('CarrinhoUser', related_name='pedido_carrihno', on_delete=models.CASCADE)
    forma_pagamento = models.ForeignKey('FormaPagamento', related_name='pedido_forma_pagamento', on_delete=models.CASCADE)
    valor_final = models.IntegerField(validators=[MinValueValidator(0)])
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.id

    def __str__(self):
        return '%s' % self.id


