# Generated by Django 3.1.1 on 2020-10-20 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0004_auto_20201020_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='current_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='donation',
            name='donation_goal',
            field=models.IntegerField(default=100),
        ),
    ]
