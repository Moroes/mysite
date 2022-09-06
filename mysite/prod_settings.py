from pathlib import Path
import os

from mysite.local_settings import DATABASES

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ku+vf+@17cfl&e+!nwlnkrge+kpyn=88888'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "158.160.5.122"]
