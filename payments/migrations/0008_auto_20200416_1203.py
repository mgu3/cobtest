# Generated by Django 2.1 on 2020-04-16 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_account_reference_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='reference_no',
            field=models.CharField(default='6169-2ffc-12d2', max_length=14, verbose_name='Reference No'),
        ),
    ]
