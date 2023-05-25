# Generated by Django 4.1.3 on 2023-05-21 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleorden',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='fecha_hora',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]