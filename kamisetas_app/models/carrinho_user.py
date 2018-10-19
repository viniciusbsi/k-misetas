# coding: utf-8
from django.db import models
# from kamisetas_app.models import Usuario
from django.core.validators import MinValueValidator


class CarrinhoUser(models.Model):
    usuario = models.ForeignKey('Usuario', related_name='carrinho_usuario', on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s' % self.id

    def __str__(self):
        return '%s' % self.id