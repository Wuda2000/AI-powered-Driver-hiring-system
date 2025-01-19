from django.urls import path
from website import views  # Import the views from your app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Ensure you have an index view
    path('drivers/', views.get_drivers, name='drivers'),  # Example API endpoint
]

# Serve static files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
