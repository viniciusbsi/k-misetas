# -*- coding: utf-8 -*-
from django.forms import *
from kamisetas_app.models import VariacaoProduto

class VariacaoProdutoForm(ModelForm):

    class Meta:
        model = VariacaoProduto
        exclude = ('excluido',)
