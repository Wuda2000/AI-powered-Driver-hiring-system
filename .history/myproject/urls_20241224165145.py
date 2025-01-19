from django.urls import path
from website import views # Import the views from your app

urlpatterns = [
    path('', views.index, name='index'),  # Ensure you have an index view
    path('drivers/', views.get_drivers, name='drivers'),  # Example API endpoint
]
