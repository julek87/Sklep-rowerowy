# Generated by Django 5.0.6 on 2024-05-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0003_remove_produkty_rezerwacja'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkty',
            name='cena',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='produkty',
            name='marka',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='produkty',
            name='model',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='produkty',
            name='opis',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='produkty',
            name='rezerwacja',
            field=models.BooleanField(default=False),
        ),
    ]