# Generated by Django 2.2.13 on 2020-06-09 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rbac", "0017_auto_20200609_1106"),
    ]

    operations = [
        migrations.RemoveField(model_name="rbacadmingrouprole", name="action",),
    ]
