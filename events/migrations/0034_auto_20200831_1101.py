# Generated by Django 3.0.9 on 2020-08-31 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0033_auto_20200831_1058"),
    ]

    operations = [
        migrations.RenameModel(old_name="BasketItems", new_name="BasketItem",),
    ]