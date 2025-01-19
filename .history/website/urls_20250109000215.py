from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('api/drivers/', views.get_drivers, name='get_drivers'),
    path('', views.index, name='index'),  # Homepage
    
]
