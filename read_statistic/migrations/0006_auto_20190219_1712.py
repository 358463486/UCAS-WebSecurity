# Generated by Django 2.1.5 on 2019-02-19 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistic', '0005_auto_20190219_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readdetail',
            name='read_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]