# Generated by Django 4.1.3 on 2023-02-21 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0002_categoria_producto_producto_delete_carro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria_producto',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
