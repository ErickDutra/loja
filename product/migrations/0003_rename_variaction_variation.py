# Generated by Django 5.0.1 on 2024-01-30 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_variaction'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Variaction',
            new_name='Variation',
        ),
    ]