# Generated by Django 3.0.9 on 2020-08-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="batch",
            name="end_time",
            field=models.DateTimeField(blank=True, null=True, verbose_name="End Time"),
        ),
    ]
