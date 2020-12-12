from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Donations posted by individuals, organizations and charities
class Donation(models.Model):
    title = models.CharField(max_length=100)
    title_processed = models.CharField(max_length=100, default="default_title")

    class CategoryChoices(models.TextChoices):
        social_justice = 'Social Justice'
        environment = 'Environment'

    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
    description = models.CharField(max_length=1000,
                                   default="Enter donation description")
    organization = models.CharField(max_length=100)
    creator = models.CharField(max_length=50, default="John")
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    start_date = models.DateTimeField('date donations started',
                                      default=datetime.datetime.now())
    length_days = models.IntegerField(default=1)
    goal = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    current_amount = models.DecimalField(max_digits=10,
                                         decimal_places=2,
                                         default=0)
    percentage_met = models.IntegerField(default=0)
    image = models.ImageField(default='/donation/images/default.png')

    def __init__(self, *args, **kwargs):
        super(Donation, self).__init__(*args, **kwargs)
        self.title_processed = self.title.replace(" ", "").lower()
        self.percentage_met = int((self.current_amount / self.goal) * 100)

    def __str__(self):
        return self.title

    def processedTitle(self):
        self.title.strip().lowercase()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(
            days=self.donation_length_days) <= self.start_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

# Individual donations payed by individuals
class IndividualDonation(models.Model):
    def __init__(self, *args, **kwargs):
        super(IndividualDonation, self).__init__(*args, **kwargs)
        if self.user == "":
            self.user = "anonymous"

    user = models.CharField(max_length=50, default="John")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    title = models.CharField(max_length=100, default="placeholder")
