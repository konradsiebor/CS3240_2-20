# Generated by Django 3.1.1 on 2020-11-19 22:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0026_merge_20201119_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 17, 41, 15, 937106), verbose_name='date donations started'),
        ),
    ]
