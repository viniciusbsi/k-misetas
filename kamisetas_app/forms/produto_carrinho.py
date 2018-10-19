# -*- coding: utf-8 -*-
from django.forms import *
from kamisetas_app.models import ProdutoCarrinho

class ProdutoCarrinhoForm(ModelForm):

    class Meta:
        model = ProdutoCarrinho
        exclude = ('excluido','carrinho')
