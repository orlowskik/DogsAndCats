from settings import *
from settings import BASE_DIR

import os

ALLOWED_HOSTS = [os.environ['']]

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

connection_str = { pair.split('=')[0]: pair.split('=')[1] for pair in os.environ['CONNECTION_STRING_POSTGRESQL'].split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': connection_str['name'],
        'DBNAME': connection_str['dbname'],
        'HOST': connection_str['host'],
        'USER': connection_str['user'],
        'PASSWORD': connection_str['password'],
    }
}
