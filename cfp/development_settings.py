# -*- coding: utf-8 -*-

from .settings import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG


DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.postgresql_psycopg2',
 'NAME': 'darmoactn9ipc6',
 'USER': 'jeoroaceocxqvb',
 'PASSWORD': 'EVNT7ZRX9FK1YUU0qZ67JdTAiV',
 'HOST': 'ec2-174-129-26-115.compute-1.amazonaws.com'
 }
}

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
 os.path.join(BASE_DIR, '../properties/static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'