from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.urls import reverse

from django.utils import timezone
from .models import Donation, IndividualDonation
from .forms import CreateForm
import decimal

from google.oauth2 import id_token
from google.auth.transport import requests


def index(request):
    return HttpResponse("Hello, world. You're at the donation index.")


def main_redirect(request):
    response = redirect("/donation/")
    return response


class HomepageView(ListView):
    template_name = "donation/home.html"
    context_object_name = 'site_wide_stats'

    def get_queryset(self):
        donation_count = 0
        donation_total = 0.0
        for donation in Donation.objects.all():
            donation_count += 1
            donation_total = donation_total + float(donation.current_amount)
        return [
            "Number of donations: {}".format(donation_count),
            "Total amount donated: {}".format(donation_total)
        ]


class DonationsListView(ListView):
    template_name = 'donation/index.html'
    context_object_name = 'active_donation_list'

    def get_queryset(self):
        return Donation.objects.filter(
            start_date__lte=timezone.now()).order_by('-start_date')
        # return Donation.objects.all()

#made obsolete with new filtering

#class DonationsListEnvironmentalView(ListView):
#    template_name = 'donation/index.html'
#    context_object_name = 'active_donation_list'

#    def get_queryset(self):
#        return Donation.objects.filter(
#            start_date__lte=timezone.now(),
#            category='Environment').order_by('-start_date')
        # return Donation.objects.all()


#class DonationsListSocialJusticeView(ListView):
#    template_name = 'donation/index.html'
#    context_object_name = 'active_donation_list'

#    def get_queryset(self):
#        return Donation.objects.filter(
#            start_date__lte=timezone.now(),
#            category='Social Justice').order_by('-start_date')
        # return Donation.objects.all()


class DonationsDetailView(DetailView):
    model = Donation
    template_name = 'donation/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Donation.objects.filter(start_date__lte=timezone.now())


class DonationCreateView(TemplateView):
    model = Donation
    template_name = 'donation/create.html'


class LeaderboardView(ListView):
    model = Donation
    context_object_name = 'top_5_donations'
    template_name = 'donation/leaderboard.html'

    def get_context_data(self, **kwargs):
        context = super(LeaderboardView, self).get_context_data(**kwargs)
        context.update({
            'individual_donations':
            IndividualDonation.objects.order_by('-amount')[:5]
        })
        return context

    def get_queryset(self):
        return Donation.objects.filter(
            start_date__lte=timezone.now()).order_by('-current_amount')[:5]


class ProfileView(ListView):
    model = IndividualDonation
    template_name = 'donation/profile.html'
    context_object_name = 'individual_donations'

    #if (request.GET.get('DeleteButton')):
    #    Donation.objects.filter(id = request.GET.get('DeleteButton')).delete()
    #    HttpResponseRedirect(reverse('donation:profile'))

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            'created_donations':
            Donation.objects.filter(
            start_date__lte=timezone.now()).filter(creator=self.request.user)[:5]
        })
        return context

    def get_queryset(self):
        return IndividualDonation.objects.filter(user=self.request.user)[:5]

def payment(request):
    donation_id = request.POST['dono_id']
    donation_amount = decimal.Decimal(request.POST['dono_amount'])
    dono = get_object_or_404(Donation, pk=donation_id)
    dono.current_amount += donation_amount
    dono.save()
    individual_donation = IndividualDonation(
        user=request.POST['user'],
        amount=request.POST['dono_amount'],
        title=request.POST['dona_title'])
    individual_donation.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('donation:donations_list'))

def categoryFilter(request):
	#if(filt == 'N/A'):
	#	filteredDonations = Donation.objects.all()
	#else:
	#	filteredDonations = Donation.objects.filter(state = request.GET.get('FilterButton'))
	#return render(request, 'donation/index.html', {'active_donation_list':filteredDonations, 'filterval': filt})



    if request.method == 'POST':
        if(request.POST.get('state') == 'N/A' and request.POST.get('categories') == 'N/A'):
            filteredDonations = Donation.objects.all()
        elif (request.POST.get('state') != 'N/A' and request.POST.get('categories') != 'N/A'):
            filteredDonations = Donation.objects.filter(state = request.POST.get('state'), category = request.POST.get('categories'))
        elif (request.POST.get('state') == 'N/A' and request.POST.get('categories') != 'N/A'):
            filteredDonations = Donation.objects.filter(category = request.POST.get('categories'))
        elif(request.POST.get('state') != 'N/A' and request.POST.get('categories') == 'N/A'):
            filteredDonations = Donation.objects.filter(state = request.POST.get('state'))
    return render(request, 'donation/index.html', {'active_donation_list':filteredDonations})



def create_donation(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            if "image1" not in form.cleaned_data or not form.cleaned_data[
                    "image1"]:
                d = Donation(title=form.cleaned_data['title'],
                             organization=form.cleaned_data['organization'],
                             creator=request.user,
                             city=form.cleaned_data['city'],
                             state=form.cleaned_data['state'],
                             description=form.cleaned_data['description'],
                             category=form.cleaned_data['category'],
                             goal=form.cleaned_data['goal'],
                             length_days=form.cleaned_data['length'])
            else:
                d = Donation(title=form.cleaned_data['title'],
                             organization=form.cleaned_data['organization'],
                             creator=request.user,
                             city=form.cleaned_data['city'],
                             state=form.cleaned_data['state'],
                             description=form.cleaned_data['description'],
                             category=form.cleaned_data['category'],
                             goal=form.cleaned_data['goal'],
                             length_days=form.cleaned_data['length'],
                             image=form.cleaned_data['image1'])
            d.save()
    return HttpResponseRedirect(reverse('donation:donations_list'))

def delete_button(request):
    print(request.GET.get('DeleteButton'))
    Donation.objects.filter(id = request.GET.get('DeleteButton')).delete()
    return HttpResponseRedirect(reverse('donation:profile_info'))