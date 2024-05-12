# Generated by Django 5.0.6 on 2024-05-11 14:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0006_rename_model_marka_marka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkty',
            name='marka',
        ),
        migrations.AddField(
            model_name='produkty',
            name='producent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.marka'),
        ),
    ]
