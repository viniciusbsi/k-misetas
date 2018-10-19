# -*- coding: utf-8 -*-
from django.views.generic import *
from kamisetas_app.models import Produto
from kamisetas_app.forms import ProdutoForm

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/produto_create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ProdutoCreateView, self).get_context_data(**kwargs)
        # context['evento_id'] = self.kwargs["evento"]
        return context

    def form_invalid(self, form):
        print(form.errors)
        return super(ProdutoCreateView, self).form_invalid(form)


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(ProdutoCreateView, self).form_valid(form)

    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(
    #         cleaned_data,
    #         nome=self.object.nome,
    #     )
