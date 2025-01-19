from django.contrib import admin
from django.urls import path, include  # Include the app URLs
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),  # Include the app's URL config
    
]
