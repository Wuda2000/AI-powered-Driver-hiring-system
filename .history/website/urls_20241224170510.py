from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page, renders index.html
    path('api/drivers/', views.get_drivers, name='get_drivers'),  # API endpoint to get drivers as JSON
]
