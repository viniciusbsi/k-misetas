# coding: utf-8
from django.db import models
from kamisetas_app.models.carrinho_user import CarrinhoUser
from kamisetas_app.models.produto import Produto
from django.core.validators import MinValueValidator


class ProdutoCarrinho(models.Model):
    carrinho = models.ForeignKey('CarrinhoUser', related_name='produto_carrinho_carrinho', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', related_name='produto_carrinho_produto', on_delete=models.CASCADE)
    qtd_produto = models.IntegerField(validators=[MinValueValidator(0)])

    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.id

    def __str__(self):
        return '%s' % self.id