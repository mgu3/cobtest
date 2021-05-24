# Generated by Django 2.1 on 2020-03-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterpointDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_number', models.IntegerField(db_index=True, verbose_name='ABF Number')),
                ('mps', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Masterpoints')),
                ('posting_month', models.IntegerField(verbose_name='Posting Month')),
                ('posting_year', models.IntegerField(verbose_name='Posting Year')),
                ('posting_date', models.TextField(max_length=7)),
                ('posting_date_display', models.TextField(max_length=8)),
                ('mp_colour', models.TextField(max_length=1)),
                ('event_description', models.TextField(max_length=50)),
                ('event_code', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MasterpointsClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_number', models.IntegerField(db_index=True, verbose_name='Club Number')),
                ('club_name', models.TextField(max_length=100, verbose_name='Club Name')),
            ],
        ),
        migrations.CreateModel(
            name='MasterpointsCopy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abf_number', models.IntegerField(blank=True, null=True, verbose_name='ABF Number')),
                ('surname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Surname')),
                ('given_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='First Name')),
                ('home_club', models.CharField(blank=True, max_length=10, null=True, verbose_name='Home Club Number')),
                ('rank', models.CharField(blank=True, max_length=50, null=True, verbose_name='Rank')),
                ('gender', models.CharField(blank=True, max_length=1, null=True, verbose_name='Gender')),
                ('active', models.BooleanField(blank=True, null=True, verbose_name='Active')),
                ('total_MPs', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total MPs')),
                ('total_gold', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Gold')),
                ('total_red', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Red')),
                ('total_green', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total Green')),
                ('month_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Monthly Total')),
                ('month_gold', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Monthly Gold')),
                ('month_red', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Monthly Red')),
                ('month_green', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Monthly Green')),
                ('this_year', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='This Year')),
                ('last_year', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Last Year')),
                ('prior', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Prior')),
                ('pre82_red', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Pre-82 Red')),
                ('year_start_rank', models.CharField(blank=True, max_length=10, null=True, verbose_name='Year Start Rank')),
                ('current_rank_seq', models.CharField(blank=True, max_length=1, null=True, verbose_name='Current Rank Sequence')),
                ('year_start_rank_seq', models.CharField(blank=True, max_length=1, null=True, verbose_name='Year Start Rank Sequence')),
                ('last_promotion_date', models.CharField(blank=True, max_length=10, null=True, verbose_name='Last Promotion Date')),
            ],
        ),
    ]