from .base import *
import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = bool(os.environ.get("DJANGO_DEBUG", default=0))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS","127.0.0.1").split(",")

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{}'.format(
            os.getenv('DATABASE_ENGINE')
        ),
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USERNAME'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}

CSRF_TRUSTED_ORIGINS = os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS', 'http://localhost:8000').split(',')