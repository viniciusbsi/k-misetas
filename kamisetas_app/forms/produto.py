# -*- coding: utf-8 -*-
from django.forms import *
from kamisetas_app.models import Produto
from kamisetas_app.models import VariacaoProduto
from django.contrib.auth.models import Permission

class ProdutoForm(ModelForm):
    variacao = ModelMultipleChoiceField(queryset=VariacaoProduto.objects.all())

    class Meta:
        model = Produto
        exclude = ('excluido',)
