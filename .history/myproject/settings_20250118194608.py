import os
from pathlib import Path
import environ

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Add the allowed hosts for local development
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


BASE_DIR = Path(__file__).resolve().parent.parent

# Path to static files (CSS, JavaScript, etc.)
STATIC_URL = '/static/'  # URL for serving static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Add path to static directory

# Directory where static files will be collected in production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

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

# Create an environ.Env instance
# Initialize environ instance
env = environ.Env()

# Ensure .env file is located in the right place
env_file_path = os.path.join(os.path.dirname(__file__), '.env')

# Read the .env file
environ.Env.read_env(env_file_path)

# Debug: Print all the loaded environment variables
print("Loaded Environment Variables:", dict(env.ENVIRON))




# Access the DB_NAME variable
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

# Time zone configuration
TIME_ZONE = 'UTC'

# Language configuration
LANGUAGE_CODE = 'en-us'

# Use Django's internationalization support (optional)
USE_I18N = True

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
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Correct middleware
]

# Root URL configuration (this tells Django where to look for URL routing)
ROOT_URLCONF = 'myproject.urls'

# WSGI application
WSGI_APPLICATION = 'myproject.wsgi.application'

LOGOUT_REDIRECT_URL = '/'

# settings.py


# settings.py

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'website.CustomUser'

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'