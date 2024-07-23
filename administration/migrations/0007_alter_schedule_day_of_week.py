# Generated by Django 5.0.6 on 2024-07-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administration", "0006_alter_schedule_day_of_week"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="day_of_week",
            field=models.IntegerField(
                choices=[
                    (1, "Lundi"),
                    (2, "Mardi"),
                    (3, "Mercredi"),
                    (4, "Jeudi"),
                    (5, "Vendredi"),
                    (6, "Samedi"),
                    (7, "Dimanche"),
                ],
                default=1,
            ),
        ),
    ]
