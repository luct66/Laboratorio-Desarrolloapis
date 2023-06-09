# Generated by Django 4.1.3 on 2023-05-20 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='detalleorden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=8)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.producto')),
            ],
        ),
    ]
