# Generated by Django 3.1.1 on 2020-10-20 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donations',
            name='location',
        ),
    ]
