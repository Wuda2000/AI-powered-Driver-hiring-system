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
        'NAME': 'driver_hiring',  # Change this to your DB name
        'USER': 'root',  # Your DB user
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

document.addEventListener('DOMContentLoaded', function() {
    // Language Selection
    const languageSelect = document.getElementById('language-select');
    languageSelect.addEventListener('change', function(event) {
        const selectedLanguage = event.target.value;
        console.log('Language selected:', selectedLanguage);
        // You can implement further logic for language change here
    });

    // Account Icon - Display Profile Picture on Login
    const profilePic = document.getElementById('profile-pic');
    const accountIcon = document.getElementById('account-icon');
    
    // Simulate profile login (you can replace this with actual login status check)
    const loggedIn = true; // Replace with real condition to check login status
    const profileImageUrl = "path/to/profile-picture.jpg"; // Replace with actual profile picture URL
    
    if (loggedIn) {
        accountIcon.style.display = 'none'; // Hide account icon if logged in
        profilePic.src = profileImageUrl;  // Set profile picture source
        profilePic.style.display = 'inline-block'; // Show profile picture
    } else {
        profilePic.style.display = 'none'; // Hide profile picture if not logged in
    }

    // Account Dropdown Menu
    const accountDropdown = document.getElementById('account-dropdown');
    accountIcon.addEventListener('click', function() {
        accountDropdown.style.display = accountDropdown.style.display === 'block' ? 'none' : 'block';
    });

    // Close dropdown if clicked outside
    document.addEventListener('click', function(event) {
        if (!accountIcon.contains(event.target)) {
            accountDropdown.style.display = 'none';
        }
    });
});
