# -*- coding: utf-8 -*-
from django.views.generic import *
from kamisetas_app.models import VariacaoProduto
from kamisetas_app.forms import VariacaoProdutoForm

class VariacaoProdutoCreateView(CreateView):
    model = VariacaoProduto
    form_class = VariacaoProdutoForm
    template_name = 'produto/variacao_produto_create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(VariacaoProdutoCreateView, self).get_context_data(**kwargs)
        return context

    def form_invalid(self, form):
        print(form.errors)
        return super(VariacaoProdutoCreateView, self).form_invalid(form)


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(VariacaoProdutoCreateView, self).form_valid(form)
