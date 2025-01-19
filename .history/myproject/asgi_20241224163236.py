import os
from django.core.asgi import get_asgi_application

# Set the default settings module for the 'DJANGO_SETTINGS_MODULE' environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Create an ASGI application for the project
application = get_asgi_application()
