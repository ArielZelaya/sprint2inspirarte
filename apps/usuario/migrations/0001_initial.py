# Generated by Django 2.0.6 on 2018-09-13 14:18

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dui', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=500)),
                ('tipo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('fechaCelebracion', models.DateField()),
                ('duracion', models.CharField(max_length=50)),
                ('fechaInicio', models.DateField()),
                ('fechaFinal', models.DateField()),
                ('horaEntrada', models.CharField(max_length=10)),
                ('horaSalida', models.CharField(max_length=10)),
                ('diasLaborales', models.CharField(max_length=135)),
                ('salario', models.FloatField()),
                ('vigente', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Contrato',
                'verbose_name_plural': 'Contratos',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dui', models.IntegerField()),
                ('nit', models.IntegerField()),
                ('isss', models.IntegerField()),
                ('nup', models.IntegerField()),
                ('codigo', models.CharField(max_length=6)),
                ('domicilio', models.CharField(max_length=500)),
                ('telefono', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('funcion', models.CharField(max_length=500)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Departamento')),
            ],
            options={
                'verbose_name': 'Puesto',
                'verbose_name_plural': 'Puestos',
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Puesto'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Empleado'),
        ),
    ]
