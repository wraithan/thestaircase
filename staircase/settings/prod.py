from os import getenv

from .base import *


TEMPLATE_DEBUG = DEBUG
SENTRY_DSN = getenv('SENTRY_DSN', None)
SITE_URL = 'thestaircase.org'
STATIC_URL = 'http://media.thestaircase.org/static/'

INSTALLED_APPS += ('raven.contrib.django', 'gunicorn')
