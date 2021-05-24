# Generated by Django 3.0.8 on 2020-07-27 03:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("events", "0004_congress_date_string"),
    ]

    operations = [
        migrations.AddField(
            model_name="congress",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="congress",
            name="venue_name",
            field=models.CharField(max_length=100, verbose_name="Venue Name"),
        ),
    ]
