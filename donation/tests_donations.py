from django.test import TestCase
from .models import Donation

from django.urls import reverse
import datetime
from django.utils import timezone


# Create your tests here.
class DonationModelTests(TestCase):
    
    # test obsoleted by removal of recency checks

    # def test_was_published_recently_future_donation(self):
    # was_published_recently returns True for donations that were started within the length_days period
    #    example_donation = Donation(goal=10, current_amount=0, length_days=1)
    #    self.assertEqual(example_donation.was_published_recently(), True)

    def test_donation_goal_is_positive(self):
        # ensure a generic Donation will be able to process percentage met number without failure by having nonzero goal
        example_donation = Donation()
        self.assertEqual(example_donation.goal > 0, True)

    def test_donation_total_is_zero_or_positive(self):
        # check that current amount is >= 0 for any given new donation
        example_donation = Donation()
        self.assertEqual(example_donation.current_amount >= 0, True)

    def setUp(self):
        Donation.objects.create(title='sample_donation', category='Environment', organization='DoGood Incorporated',
                                city='Charlottesville', state='Virginia')

    def test_donation_default_description_set(self):
        # check that default values are set when a new donation is created
        sample_donation = Donation.objects.get(id=1)
        expected_description = f'{sample_donation.description}'
        self.assertEquals(expected_description, 'Enter donation description')

    def test_donation_default_goal_set(self):
        sample_donation = Donation.objects.get(id=1)
        expected_goal = sample_donation.goal
        self.assertEquals(expected_goal, 100.00)

    def test_donation_default_length_set(self):
        sample_donation = Donation.objects.get(id=1)
        expected_length_days = sample_donation.length_days
        self.assertEquals(expected_length_days, 1)

    def test_donation_default_amount_set(self):
        sample_donation = Donation.objects.get(id=1)
        expected_current_amount = sample_donation.current_amount
        self.assertEquals(expected_current_amount, 0)

    def test_donation_default_percentage_set(self):
        sample_donation = Donation.objects.get(id=1)
        expected_percentage_met = sample_donation.percentage_met
        self.assertEquals(expected_percentage_met, 0)

    def test_HTML_posts_to_donations(self):
        # check that a new donation can be submitted via the HTML in donation/create.html
        response = self.client.get('/donation/create')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'donation/create.html')
