# Generated by Django 4.1.7 on 2023-04-24 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaApp', '0002_producto_created_producto_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria_producto',
            old_name='nombre_cat',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_prod',
            new_name='nombre',
        ),
    ]
