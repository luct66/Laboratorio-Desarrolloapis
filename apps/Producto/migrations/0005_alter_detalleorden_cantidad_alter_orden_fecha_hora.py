# Generated by Django 4.1.3 on 2023-06-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0004_alter_detalleorden_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleorden',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha_hora',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]