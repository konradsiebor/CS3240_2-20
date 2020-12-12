from django.contrib.auth.models import Donation
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Donation
        fields = ['category']