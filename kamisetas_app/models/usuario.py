from django.db import models

class Usuario(models.Model):
    pessoa_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return self.pessoa_usuario.get_full_name()

    def __str__(self):
        return self.pessoa_usuario.get_full_name()

