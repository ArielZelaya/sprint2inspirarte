# Generated by Django 2.0.6 on 2018-09-14 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0006_auto_20180914_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='Cotizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotizacion.Cotizacion'),
        ),
    ]
