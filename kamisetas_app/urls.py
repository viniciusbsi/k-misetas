from django.conf.urls import patterns, include, url
from kamisetas_app.views import *
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth import views

admin.autodiscover()

urlpatterns = [
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^produto/cadastrar', ProdutoCreateView.as_view(), name='produto-cadastrar'),
    url(r'^variacao/produto/cadastrar', VariacaoProdutoCreateView.as_view(), name='variacao-produto-cadastrar'),
    url(r'^produto/carrinho/cadastrar', ProdutoCarrinhoCreateView.as_view(), name='produto-carrinho-cadastrar'),
    url(r'^produto/carrinho/comprar', RealizarCompraCreateView.as_view(), name='comprar-produtos-carrinho'),
    url(r'^usuario/cadastrar', UsuarioCreateView.as_view(), name='usuario-cadastrar'),
    url(r'^', TemplateView.as_view(template_name='home.html'), name='home'),
]

