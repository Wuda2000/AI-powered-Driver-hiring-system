from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/drivers/', views.get_drivers, name='get_drivers'),  # Make sure this matches the fetch URL
]
