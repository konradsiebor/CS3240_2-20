from .models import IndividualDonation
from django.test import TestCase


class IndividualDonationModelTest(TestCase):

    def test_user_name_set(self):
        # check that every individual donation is successfully attributed a user name
        example_individual = IndividualDonation()
        check = isinstance(example_individual.user, str)
        self.assertEquals(check, True)

    def test_individual_positive(self):
        # check that current amount is >= 0 for any given individual donation
        example_individual = Donation()
        self.assertEqual(example_individual.amount >= 0, True)

     def test_donation_title(self):
        # check that every individual donation is successfully attributed to a donation
        example_individual = IndividualDonation()
        check = isinstance(example_individual.title, str)
        self.assertEquals(check, True)