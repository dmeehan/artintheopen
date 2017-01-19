# settings/base.py

import os
from datetime import timedelta
from os.path import abspath, basename, dirname, join, normpath
from sys import path

from django.core.urlresolvers import reverse_lazy

#==============================================================================
# Path 
#==============================================================================

# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Absolute filesystem path to project container folder:
PROJECT_ROOT = dirname(SITE_ROOT) 

# Absolute filesystem path to project container folder:
APP_ROOT = normpath(join(DJANGO_ROOT, 'apps')),

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
path.append(APP_ROOT)


#==============================================================================
# Managers 
#==============================================================================

ADMINS = (
    ('Douglas Meehan', 'dmeehan@gmail.com'),
)

MANAGERS = ADMINS

#==============================================================================
# Site 
#==============================================================================

SITE_ID = 2

# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

#==============================================================================
# Debugging
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
#TEMPLATE_DEBUG = DEBUG


#==============================================================================
# Secret Key 
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '87hq#$x_zu_=r)polio0q1y*$ii2z4wt82cqpx=167wt4lsa83$')


#==============================================================================
# Localization
#==============================================================================

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True    #internationalization machinery
USE_L10N = True    #format dates, numbers and calendars according to locale
USE_TZ = True

#==============================================================================
# Database Configuration
#==============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

#==============================================================================
# Fixtures
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)


#==============================================================================
# Static assets
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(PROJECT_ROOT, 'static'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
]

COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]

#==============================================================================
# Uploaded assets 
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(PROJECT_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

#==============================================================================
# Templates
#==============================================================================


# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(DJANGO_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },

    },
]

#==============================================================================
# Middleware
#==============================================================================


# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]


#==============================================================================
# Project URLS
#==============================================================================


# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'urls'



#==============================================================================
# Messages
#==============================================================================

#MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


#==============================================================================
# Authentication
#==============================================================================

#AUTH_USER_MODEL = 'auth.User'
#LOGIN_URL = reverse_lazy('admin:index')


#==============================================================================
# Installed Apps
#==============================================================================

INSTALLED_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    # admin apps
    'grappelli',# must go before admin
    'tinymce',
    'django.contrib.admin',
    'filebrowser',

    'django_comments',
    'localflavor',
    'compressor', # static file management
    'djsupervisor', # process mgmt

    'about',
    'affiliates',
    'artists',
    'cms',
    'events',
    'home',
    'locations'   
)
    
    

#==============================================================================
# Logging
#==============================================================================

 
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

#==============================================================================
# Server Configuration
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'

SERVER_PORT = os.environ.get("SERVER_PORT", "8000")

#==============================================================================
# Compression 
#==============================================================================


COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_ENABLED

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]

#==============================================================================
# Caching
#==============================================================================

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


#==============================================================================
# Admin
#==============================================================================

GRAPPELLI_ADMIN_TITLE = 'Art in the Open'
#GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

#==============================================================================
# Front End Assets
#==============================================================================

#==============================================================================
# Local App Configuration
#==============================================================================
MAPS_API_KEY = os.environ.get('MAPS_API_KEY', 'ABQIAAAAayJegR1S7-F1AMio1LsppBQQQy_sjnlSHoxZX2FsIIn-z7Y4GhQYU4F7ksh264zpeovV7XSOmhcBfw')

COMMENTS_AKISMET_API_KEY = '7cbaf5969a99'
COMMENTS_MODERATE_AFTER = 30 
COMMENTS_CLOSE_AFTER = 0

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 540, 'height': '', 'opts': ''},
}