# Generated by Django 2.1.2 on 2018-10-19 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kamisetas_app', '0004_auto_20181019_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='variacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='produto_variacao', to='kamisetas_app.VariacaoProduto'),
            preserve_default=False,
        ),
    ]
