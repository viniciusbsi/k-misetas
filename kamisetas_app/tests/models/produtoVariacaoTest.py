from django.test import TestCase
from django.contrib.auth.models import User
from kamisetas_app.models.variacao_produto import VariacaoProduto

class VaricaoProdutoTest(TestCase):


    def setUp(self):
        self.varicaoProduto = VariacaoProduto.objects.create(
            descricao="DescricaoProdutoTeste",
            preco=12.00, 
            qtd_estoque=200)
    
    def tearDown(self):
        self.varicaoProduto.delete()
    
    def testObjectsCreatedVariacaoProduto(self):
        self.assertEquals(VariacaoProduto.objects.count(), 1)

    def testQuantiadeVariacaoProduto(self):
        self.assertEquals(self.varicaoProduto.qtd_estoque, 200)
    
    def testPrecoProduto(self):
        self.assertEquals(self.varicaoProduto.preco, "DescricaoProdutoTeste")

    def testDescricaoProduto(self):
        self.assertEquals(self.varicaoProduto.descricao, 12.00)
