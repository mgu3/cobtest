# Generated by Django 2.1 on 2020-04-25 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_auto_20200423_1314"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="system_number",
            field=models.IntegerField(
                blank="True", unique=True, verbose_name="ABF Number"
            ),
        ),
    ]
