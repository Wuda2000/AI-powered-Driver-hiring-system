from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('api/drivers/', views.get_drivers, name='get_drivers'),
    path('', views.index, name='index'),  # Homepage
    path('about-us/', views.about_us_view, name='about_us'),
    path('services/', views.services_view, name='services'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('clients/', views.clients_view, name='clients'),
    path('contact/', views.contact_view, name='contact'),
]
