# -*- coding: utf-8 -*-
from django.views.generic import *
from kamisetas_app.models import ProdutoCarrinho
from kamisetas_app.forms import ProdutoCarrinhoForm

class ProdutoCarrinhoCreateView(CreateView):
    model = ProdutoCarrinho
    form_class = ProdutoCarrinhoForm
    template_name = 'produto/produto_carrinho.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ProdutoCarrinhoCreateView, self).get_context_data(**kwargs)
        return context

    def form_invalid(self, form):
        print(form.errors)
        return super(ProdutoCarrinhoCreateView, self).form_invalid(form)


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(ProdutoCarrinhoCreateView, self).form_valid(form)
