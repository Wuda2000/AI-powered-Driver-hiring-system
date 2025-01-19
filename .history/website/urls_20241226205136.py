from django.urls import path
from . import views

urlpatterns = [
    path('api/drivers/', views.get_drivers, name='get_drivers'),
    path('', views.index, name='index'),  # Ensure this maps to the index view
]
