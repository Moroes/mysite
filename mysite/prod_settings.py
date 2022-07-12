from pathlib import Path
import os

from mysite.local_settings import DATABASES

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ku+vf+@17cfl&e+!nwlnkrge+kpyn=88888'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'main',
        'USER': 'moroes',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]