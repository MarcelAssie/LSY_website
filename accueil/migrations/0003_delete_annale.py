# Generated by Django 5.0.6 on 2024-07-21 15:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accueil", "0002_annale_delete_band"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Annale",
        ),
    ]
