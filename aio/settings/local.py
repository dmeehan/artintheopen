# settings/local.py

from os import environ
from os.path import join, normpath

from base import *

#==============================================================================
# Debugging
#==============================================================================

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'dev.artintheopenphila.org']


#==============================================================================
# Email Configuration
#==============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#==============================================================================
# Caching
#==============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

#==============================================================================
# Installed Apps
#==============================================================================

INSTALLED_APPS += (
	'debug_toolbar',  
)

#==============================================================================
# Toolbar Configuration
#==============================================================================

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)





#==============================================================================
# Celery Configuration
#==============================================================================


# See: http://docs.celeryq.org/en/latest/configuration.html#celery-always-eager
CELERY_ALWAYS_EAGER = True

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-eager-propagates-exceptions
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
