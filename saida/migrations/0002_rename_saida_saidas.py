# Generated by Django 5.0.4 on 2024-06-09 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
        ('saida', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Saida',
            new_name='Saidas',
        ),
    ]
