# coding: utf-8
from django.db import models
# from kamisetas_app.models import Usuario
from django.core.validators import MinValueValidator


class CarrinhoUser(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s' % self.usuario.get_full_name()

    def __str__(self):
        return '%s' % self.usuario.get_full_name()