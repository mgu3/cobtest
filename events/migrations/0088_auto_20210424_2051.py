# Generated by Django 3.0.9 on 2021-04-24 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0087_auto_20210409_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evententry',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Category'),
        ),
    ]
