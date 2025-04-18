"""
Django settings for real_estate project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# Import external libraries for environment variable handling and file path management.
import environ  # Library for reading environment variables from a .env file.
from pathlib import Path  # Provides classes to work with file system paths.

# Initialize environment variables with default settings.
env = environ.Env(
    DEBUG=(bool, False)  # Default value for DEBUG is False.
)

# Define BASE_DIR to reference the root directory of the project.
# This is built relative to this settings file: three levels up from the current file.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables from a .env file located at the project root.
environ.Env.read_env(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')  # Read the SECRET_KEY from the .env file.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')  # Read DEBUG setting from environment variables.

# ALLOWED_HOSTS: Hosts/domain names that this Django site can serve.
# It reads a space-separated list from the environment variable and splits it into a list.
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(' ')


# Application definition

# List of Django's built-in applications.
DJANGO_APPS = [
    'django.contrib.admin',         # Admin site.
    'django.contrib.auth',          # Authentication framework.
    'django.contrib.contenttypes',  # Content type framework.
    'django.contrib.sessions',      # Session framework.
    'django.contrib.messages',      # Messaging framework.
    'django.contrib.staticfiles',   # Management of static files.
    'django.contrib.sites',         # Sites framework.
]

# Set the current site ID for the django.contrib.sites framework.
SITE_ID = 1

# List of third-party applications added to the project.
THIRD_PARTY_APPS = [
    'rest_framework',    # Django REST framework for building APIs.
    'django_filters',    # Filtering support for Django REST framework.
    'django_countries',  # Provides country choices for models.
    'phonenumber_field', # Phone number field for Django models.
    'djoser',
    'rest_framework_simplejwt',
]

# List of local apps (custom apps developed for the project).
LOCAL_APPS  =  [
    'apps.common',
    'apps.users',
    'apps.profiles',
    'apps.ratings',
]

# Combine all applications into one list for Django to register.
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middleware definitions: a list of middleware components that process requests/responses.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',  # Provides various HTTP conveniences.
    'django.middleware.csrf.CsrfViewMiddleware',  # Cross Site Request Forgery protection.
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration module for the project.
ROOT_URLCONF = 'real_estate.urls'

# Templates configuration: settings for the template engine.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Directories where Django will search for templates.
        'APP_DIRS': True,  # Tells Django to look for templates inside installed apps.
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

# WSGI application callable for deploying with WSGI servers.
WSGI_APPLICATION = 'real_estate.wsgi.application'


# Database configuration would be placed here.
# For more information, refer to:
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


# Password validation configuration: a list of validators to enforce password policies.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization settings

# Default language code for the project.
LANGUAGE_CODE = 'en-us'

# Time zone settings; this example uses Sao Paulo time.
TIME_ZONE = 'America/Sao_Paulo'
# An alternative time zone (UTC) is commented out.
# TIME_ZONE = 'UTC'

USE_I18N = True  # Enable Django’s internationalization system.
USE_TZ = True    # Enable timezone support.

# Static files (CSS, JavaScript, Images) configuration

# URL to use when referring to static files.
STATIC_URL = '/staticfiles/'
# Directory where static files will be collected.
STATIC_ROOT = BASE_DIR / 'staticfiles'
# List of additional directories to look for static files.
STATICFILES_DIR = []

# Media files configuration (uploaded content)
MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# Default primary key field type for models.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Tell Django to use the custom user model defined in apps.users.
AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

from datetime import timedelta

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': (
        ' Bearer',
        'JWT',
    ),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'SIGNING_KEY': env('SIGNING_KEY'),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}

DJOSER ={
    'LOGIN_FIELD':'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_CONFIRMATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create': 'apps.users.serializers.CreateUserSerializer',
        'user': 'apps.users.serializers.UserSerializer',
        'current_user': 'apps.users.serializers.UserSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    }
}

# Logging configuration to capture log messages.
import logging
import logging.config
from django.utils.log import DEFAULT_LOGGING

logger = logging.getLogger(__name__)  # Logger instance for this module.

LOG_LEVEL = 'INFO'  # Set the logging level.

# Configure logging settings using a dictionary configuration.
logging.config.dictConfig({
    'version': 1,  # Configuration schema version.
    'disable_existing_loggers': False,  # Do not disable loggers that are already configured.
    'formatters': {
        # Formatter for console output.
        'console': {
            'format': '%(asctime)s %(name) -12s %(levelname)-8s %(message)s'
        },
        # Formatter for file output.
        'file': {
            'format': '%(asctime)s %(name) -12s %(levelname)-8s %(message)s'
        },
        # Use Django's default server formatter.
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
    },
    'handlers': {
        # Console handler to output logs to the console.
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        # File handler to output logs to a file.
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'logs/real_estate.log'  # Log file location.
        },
        # Use Django's default server handler.
        'django.server': DEFAULT_LOGGING['handlers']['django.server'],
    },
    'loggers': {
        # Root logger configuration.
        '': {
            'level': "INFO",
            'handlers': ['console', 'file'],
            'propagate': False,
        },
        # Logger configuration for apps; typically used for custom logging in your local apps.
        'apps': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
        # Logger for Django's server logs.
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],
    }
})
