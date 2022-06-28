# Generated by Django 4.0.5 on 2022-06-28 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_inventario_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='telefono',
            field=models.FloatField(default=django.utils.timezone.now, max_length=9, verbose_name='Telefono'),
            preserve_default=False,
        ),
    ]
