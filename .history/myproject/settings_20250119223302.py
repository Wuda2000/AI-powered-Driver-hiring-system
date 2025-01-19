#import statements 
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Add the allowed hosts for local development
ALLOWED_HOSTS = ['*']  # Allows all hosts, change this for production

# The base directory of your project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Secret key (change this to a securely generated one in production)
SECRET_KEY = 't#=_p=)&*(_z=#6ggj$k8+q#5#@d6#yk*jhy5k6w#$d#)%1tr$'

# Path to static files (CSS, JavaScript, etc.)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Add the path to your static files folder (assuming 'static' is at the project root)


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

# Database configuration (for MySQL in this case)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',  
        'USER': '',  # Remove the DB user
        'PASSWORD': '',  # Remove the DB password
        'HOST': '',  # Remove the DB host
        'PORT': '',  # Remove the DB port
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
