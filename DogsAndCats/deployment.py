from settings import *
from settings import BASE_DIR

import os

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://', os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

connection_str = {pair.split('=')[0]: pair.split('=')[1] for pair in os.environ['AZURE_POSTGRESQL_CONNECTION'].split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': connection_str['dbname'],
        'HOST': connection_str['host'],
        'USER': connection_str['user'],
        'PASSWORD': connection_str['password'],
    }
}
