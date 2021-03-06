# Generated by Django 3.1.1 on 2020-10-21 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0009_donation_percentage_met'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='current_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='donation',
            name='goal',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
