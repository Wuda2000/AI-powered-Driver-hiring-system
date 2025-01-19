from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('api/drivers/', views.get_drivers, name='get_drivers'),
    path('', views.index, name='index'),  # Homepage
    path('Aboutus.html', views.about_us_view, name='about_us_html'),
    path('Settings.html', views.services_view, name='services_html'),
    path('Pricing.html', views.pricing_view, name='pricing_html'),
    path('clients.html', views.clients_view, name='clients_html'),
    path('contact.html', views.contact_view, name='contact_html'),
    # URL pattern for Car Owners Offer Page
    path('car-owners-offer/', views.car_owners_offer, name='car-owners-offer'),

    # URL pattern for Drivers Offer Page
    path('drivers-offer/', views.drivers_offer, name='drivers-offer'),

     # URL pattern for Objective Page
    path('objective/', views.objective, name='objective'),

    # URL pattern for Feedback Page
    path('feedback/', views.feedback, name='feedback'),

    # URL pattern for Ratings Page
    path('ratings/', views.ratings, name='ratings'),
]
