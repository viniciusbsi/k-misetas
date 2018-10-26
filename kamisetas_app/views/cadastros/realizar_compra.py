# -*- coding: utf-8 -*-
from django.views.generic import *
from kamisetas_app.models import ProdutoCarrinho, CarrinhoUser
from kamisetas_app.forms import ProdutoCarrinhoForm

class RealizarCompraCreateView(CreateView):
    model = ProdutoCarrinho
    form_class = ProdutoCarrinhoForm
    template_name = 'produto/realizar_compra.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(RealizarCompraCreateView, self).get_context_data(**kwargs)
        carrinho_usuario = CarrinhoUser.objects.get(usuario=self.request.user.id)
        context['compras_usuario'] = ProdutoCarrinho.objects.filter(carrinho=carrinho_usuario)
        return context

    # def form_invalid(self, form):
    #     print(form.errors)
    #     return super(RealizarCompraCreateView, self).form_invalid(form)
    #
    #
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     carrinho_user = CarrinhoUser.objects.get(usuario=self.request.user.id)
    #     self.object.carrinho = carrinho_user
    #     self.object.save()
    #     return super(RealizarCompraCreateView, self).form_valid(form)
    #
