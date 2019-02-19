# Generated by Django 2.1.5 on 2019-02-17 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadDetail',
            fields=[
                ('readnum_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='read_statistic.ReadNum')),
                ('read_date', models.DateField()),
            ],
            bases=('read_statistic.readnum',),
        ),
    ]
