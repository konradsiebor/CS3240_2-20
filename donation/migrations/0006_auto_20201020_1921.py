# Generated by Django 3.1.1 on 2020-10-20 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0005_auto_20201020_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='donation_goal',
            new_name='goal',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='donation_length_days',
            new_name='length_days',
        ),
    ]