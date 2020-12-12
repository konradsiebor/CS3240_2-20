from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

from . import views

app_name = 'donation'
urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('profile', views.ProfileView.as_view(), name='profile_info'),
    path('profile/delete', views.delete_button, name='delete_donation'),
    path('filteredlist', views.categoryFilter, name='filt'),
    path('list', views.DonationsListView.as_view(), name='donations_list'),
    #path('envlist', views.DonationsListEnvironmentalView.as_view(), name='donations_list_environmental'),
    #path('socjustlist', views.DonationsListSocialJusticeView.as_view(), name='donations_list_socjust'),
    path('create', views.DonationCreateView.as_view(), name='create_donation'),
    path('create/submit', views.create_donation, name='submit_donation'),
    path('leaderboard', views.LeaderboardView.as_view(), name='leaderboard_display'),
    path('list/<int:pk>/',
         views.DonationsDetailView.as_view(),
         name='donation_detail'),
    url(r'^payment/', views.payment, name='payment'),
    # path('', include('donation.urls'))
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

