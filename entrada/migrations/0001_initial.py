# Generated by Django 5.0.4 on 2024-05-20 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.FloatField(default=0, verbose_name='Preço')),
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produtos', verbose_name='Produto')),
            ],
        ),
    ]
