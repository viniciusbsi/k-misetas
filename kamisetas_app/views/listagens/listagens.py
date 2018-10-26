from django.views.generic import ListView
from kamisetas_app.models import *

class ProdutoList(ListView):
    queryset = Produto.objects.all().exclude(excluido=True)
    template_name = 'listagens/produtoLista.html'

class CarrinhoUsuarioList(ListView):
    queryset = CarrinhoUser.objects.all().exclude(excluido=True)
    template_name = 'listagens/carrinhoUsuarioLista.html'

class UserList(ListView):
    queryset = Usuario.objects.all().exclude(excluido=True)
    template_name = 'listagens/UsuarioLista.html'

class PedidoList(ListView):
    queryset = Pedido.objects.all().exclude(excluido=True)
    template_name = 'listagens/pedidoLista.html'
