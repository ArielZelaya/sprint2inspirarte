# Generated by Django 2.0.6 on 2018-09-19 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotizacion', '0012_auto_20180918_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecotizacion',
            name='archivo',
        ),
    ]
