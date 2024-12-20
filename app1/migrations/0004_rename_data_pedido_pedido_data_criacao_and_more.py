# Generated by Django 5.1.3 on 2024-12-13 01:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_itempedido_preco_unitario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='data_pedido',
            new_name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='itempedido',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
        migrations.AddField(
            model_name='itempedido',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='app1.pedido'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Concluído', 'Concluído'), ('Cancelado', 'Cancelado')], default='Pendente', max_length=20),
        ),
    ]
