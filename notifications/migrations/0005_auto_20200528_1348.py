# Generated by Django 2.2.12 on 2020-05-28 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0004_auto_20200523_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inappnotification',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='NotificationMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.CharField(max_length=20, verbose_name='Application')),
                ('topic', models.CharField(max_length=20, verbose_name='Topic')),
                ('subtopic', models.CharField(blank=True, max_length=20, null=True, verbose_name='Sub-Topic')),
                ('notification_type', models.CharField(choices=[('SMS', 'SMS Message'), ('Email', 'Email Message')], default='Email', max_length=5, verbose_name='Notification Type')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
