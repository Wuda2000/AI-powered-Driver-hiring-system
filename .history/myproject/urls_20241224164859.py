from django.urls import path
from . import views # Import the views from your app

urlpatterns = [
    path('', v.index, name='index'),  # Ensure you have an index view
    path('drivers/', views.get_drivers, name='drivers'),  # Example API endpoint
]
