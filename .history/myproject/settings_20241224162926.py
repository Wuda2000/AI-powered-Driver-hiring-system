import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Add the allowed hosts for local development
ALLOWED_HOSTS = ['*']  # Allows all hosts, change this for production

# The base directory of your project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to static files (CSS, JavaScript, etc.)
STATIC_URL = '/static/'

# Define the installed applications (add your app and necessary Django apps)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',  # Your app name here
]

# Database configuration (for MySQL in this case)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'driver_hiring',  # Change this to your DB name
        'USER': 'your_database_user',  # Your DB user
        'PASSWORD': 'James@2542003',  # Your DB password
        'HOST': 'localhost',  # Use localhost for local development
        'PORT': '3306',  # Default MySQL port
    }
}

# Time zone configuration
TIME_ZONE = 'UTC'

# Language configuration
LANGUAGE_CODE = 'en-us'

# Use Django's internationalization support (optional)
USE_I18N = True

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# If you are using templates, add the following:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Middleware configuration (optional, required by Django)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XContentOptionsMiddleware',
]

# Root URL configuration (this tells Django where to look for URL routing)
ROOT_URLCONF = 'myproject.urls'

# WSGI application
WSGI_APPLICATION = 'myproject.wsgi.application'
