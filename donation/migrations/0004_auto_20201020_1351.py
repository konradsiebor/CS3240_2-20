# Generated by Django 3.1.1 on 2020-10-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_donations_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Social Justice', 'Social Justice'), ('Environment', 'Environment')], max_length=50)),
                ('description', models.CharField(default='Enter donation description', max_length=1000)),
                ('organization', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('start_date', models.DateTimeField(verbose_name='date donations started')),
                ('donation_length_days', models.IntegerField(default=1)),
            ],
        ),
        migrations.RenameModel(
            old_name='IndividualDonations',
            new_name='IndividualDonation',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='Donations',
        ),
    ]
