# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('kamisetas_app', '0005_auto_20181019_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinhouser',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
