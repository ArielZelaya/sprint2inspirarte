# Generated by Django 2.0.6 on 2018-09-14 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0007_auto_20180914_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='Cotizacion',
        ),
    ]