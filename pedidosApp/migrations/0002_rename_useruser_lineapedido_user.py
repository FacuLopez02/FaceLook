# Generated by Django 4.1.7 on 2023-04-29 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidosApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lineapedido',
            old_name='useruser',
            new_name='user',
        ),
    ]
