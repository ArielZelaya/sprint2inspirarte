# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-10 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '__first__'),
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('total', models.FloatField(null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Cliente')),
            ],
            options={
                'verbose_name': 'Cotizacion',
                'verbose_name_plural': 'Cotizaciones',
            },
        ),
        migrations.CreateModel(
            name='DetalleCotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('tamaño', models.CharField(max_length=25)),
                ('subtotal', models.FloatField(null=True)),
                ('disenio', models.BooleanField()),
                ('archivo', models.FileField(upload_to='uploads/%Y-%m-%d/%H_%M_%S')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('activo', models.BooleanField()),
                ('precio', models.FloatField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='detallecotizacion',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotizacion.TipoProducto'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='detalle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotizacion.DetalleCotizacion'),
        ),
    ]