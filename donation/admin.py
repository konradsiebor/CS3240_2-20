from django.contrib import admin
from .models import Donation, IndividualDonation

# Register your models here.

admin.site.register(Donation)
admin.site.register(IndividualDonation)