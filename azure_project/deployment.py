import os

from .settings import *

from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]

CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]

DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoite.middleware.WhiteNoiseMiddeleware',
]

STATICFILES_STOREGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


#connection_string - os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "Postgres",
        "USER": os.getenv('PGUSER'),
        "PASSWORD": os.getenv('PGPASSWORD'),
        "HOST": os.getenv('PGHOST'),
        "PORT": os.getenv('PGPORT'),
    }
}
