from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ku+vf+@17cfl&e+!nwlnkrge+kpyn=88888'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'main',
        'USER': 'postgres',
        'PASSWORD': 'asdhfgjk23821',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]