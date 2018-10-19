from django.contrib import admin
from kamisetas_app.models import *

# Register your models here.
admin.site.register(ProdutoCarrinho)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Usuario)
admin.site.register(FormaPagamento)
admin.site.register(VariacaoProduto)
admin.site.register(CarrinhoUser)