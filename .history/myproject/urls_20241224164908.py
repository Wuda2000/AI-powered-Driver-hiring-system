from django.urls import path
from . import views # Import the views from your app

urlpatterns = [
    path('', views.index, name='index'),  # Ensure you have an index view
    path('drivers/', v.get_drivers, name='drivers'),  # Example API endpoint
]
