# Generated by Django 5.0.7 on 2024-07-26 22:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_parent", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rendezvous",
            name="autre_motif",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
