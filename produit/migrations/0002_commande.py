# Generated by Django 5.1.2 on 2024-11-13 15:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description_cmd', models.CharField(max_length=50)),
                ('Date_cmd', models.DateField(default=django.utils.timezone.now)),
                ('Produit_cmd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produit.product')),
            ],
        ),
    ]
