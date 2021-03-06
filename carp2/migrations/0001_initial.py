# Generated by Django 2.2.17 on 2020-12-13 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarios', models.CharField(max_length=30)),
                ('Contrasenia', models.CharField(max_length=30)),
                ('Roles', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=30)),
                ('Descripcion', models.CharField(max_length=300)),
                ('Existencia', models.IntegerField()),
                ('Precio', models.FloatField()),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carp2.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Cliente', models.CharField(max_length=100)),
                ('serie', models.IntegerField()),
                ('nit', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('total', models.FloatField()),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='carp2.producto')),
            ],
        ),
    ]
