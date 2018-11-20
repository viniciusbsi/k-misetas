from django.test import TestCase
from django.contrib.auth.models import User
from kamisetas_app.models import Usuario

class UserTest(TestCase):
    

    def setUp(self):
        self.user = User.objects.create_user(
            username="test", 
            email="test@test.com", 
            password="test")

        self.usuario = Usuario.objects.create(pessoa_usuario=self.user)
    
    def tearDown(self):
        self.user.delete()
        self.usuario.delete()

    
    def testObjectsCreatedUser(self):
        self.assertEquals(User.objects.count(), 1)


    def testObjectsCreatedUserio(self):
        self.assertEquals(Usuario.objects.count(), 1)