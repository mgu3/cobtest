# Generated by Django 3.0.9 on 2020-10-12 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0053_remove_congress_default_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="free_format_question",
            field=models.CharField(
                blank=True,
                max_length=60,
                null=True,
                verbose_name="Free Format Question",
            ),
        ),
        migrations.AddField(
            model_name="evententry",
            name="free_format_answer",
            field=models.CharField(
                blank=True, max_length=60, null=True, verbose_name="Free Format Answer"
            ),
        ),
    ]