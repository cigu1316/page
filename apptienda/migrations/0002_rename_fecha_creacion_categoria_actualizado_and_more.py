# Generated by Django 4.1.3 on 2023-02-20 02:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apptienda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='fecha_creacion',
            new_name='actualizado',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='estado',
            new_name='disponibilidad',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='stock',
        ),
        migrations.AddField(
            model_name='categoria',
            name='creado',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
