# Generated by Django 3.1 on 2020-08-19 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0016_auto_20200818_1656"),
    ]

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("session_date", models.DateField(blank=True, null=True)),
                ("session_start", models.TimeField(blank=True, null=True)),
                ("session_end", models.TimeField(blank=True, null=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.event"
                    ),
                ),
            ],
        ),
    ]
