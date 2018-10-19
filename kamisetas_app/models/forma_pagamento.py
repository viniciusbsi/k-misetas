# coding: utf-8
from django.db import models

class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=200)
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.id

    def __str__(self):
        return '%s' % self.id