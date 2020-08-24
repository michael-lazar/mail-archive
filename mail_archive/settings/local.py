# -*- coding: utf-8 -*-
import os
from django.contrib.messages import constants as messages  # flake8: noqa

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'change-this-on-your-production-server'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = (
     ('HyperKitty Admin', 'root@localhost'),
)

SITE_ID = 1

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

INSTALLED_APPS = (
    'hyperkitty',
    'django_mailman3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_gravatar',
    'compressor',
    'haystack',
    'django_extensions',
    'django_q',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_mailman3.lib.auth.fedora',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_mailman3.middleware.TimezoneMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.csrf',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_mailman3.context_processors.common',
                'hyperkitty.context_processors.common',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'hyperkitty.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # BASE_DIR + '/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Django 1.6+ defaults to a JSON serializer, but it won't work with
# django-openid, see
# https://bugs.launchpad.net/django-openid-auth/+bug/1252826
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'hk_root'
LOGOUT_URL = 'account_logout'


MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

#
# Gravatar
# https://github.com/twaddington/django-gravatar
#
# Gravatar base url.
# GRAVATAR_URL = 'http://cdn.libravatar.org/'
# Gravatar base secure https url.
# GRAVATAR_SECURE_URL = 'https://seccdn.libravatar.org/'
# Gravatar size in pixels.
# GRAVATAR_DEFAULT_SIZE = '80'
# An image url or one of the following: 'mm', 'identicon', 'monsterid',
# 'wavatar', 'retro'.
# GRAVATAR_DEFAULT_IMAGE = 'mm'
# One of the following: 'g', 'pg', 'r', 'x'.
# GRAVATAR_DEFAULT_RATING = 'g'
# True to use https by default, False for plain http.
# GRAVATAR_DEFAULT_SECURE = True

#
# django-compressor
# https://pypi.python.org/pypi/django_compressor
#
COMPRESS_PRECOMPILERS = (
   ('text/x-scss', 'sassc -t compressed {infile} {outfile}'),
   ('text/x-sass', 'sassc -t compressed {infile} {outfile}'),
)
# On a production setup, setting COMPRESS_OFFLINE to True will bring a
# significant performance improvement, as CSS files will not need to be
# recompiled on each requests. It means running an additional "compress"
# management command after each code upgrade.
# http://django-compressor.readthedocs.io/en/latest/usage/#offline-compression
# COMPRESS_OFFLINE = True

# Needed for debug mode
INTERNAL_IPS = ('127.0.0.1',)


#
# Full-text search engine
#
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, "fulltext_index"),
        # You can also use the Xapian engine, it's faster and more accurate,
        # but requires another library.
        # http://django-haystack.readthedocs.io/en/v2.4.1/installing_search_engines.html#xapian
        # Example configuration for Xapian:
        #'ENGINE': 'xapian_backend.XapianEngine'
    },
}


#
# REST framework
#
REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.OrderingFilter',
    ),
}


#
# Asynchronous tasks
#
Q_CLUSTER = {
    'timeout': 300,
    'save_limit': 100,
    'orm': 'default',
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file':{
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(BASE_DIR, 'hyperkitty.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'hyperkitty': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(process)d %(name)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
}

# Using the cache infrastructure can significantly improve performance on a
# production setup. This is an example with a local Memcached server.
#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#        'LOCATION': '127.0.0.1:11211',
#    }
#}

# When DEBUG is True, don't actually send emails to the SMTP server, just store
# them in a directory. This way you won't accidentally spam your mailing-lists
# while you're fiddling with the code.
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'emails')


#
# HyperKitty-specific
#
# Only display mailing-lists from the same virtual host as the webserver
FILTER_VHOST = False

# The location of the lock file for the update_index and update_and_clean_index
# jobs can be set as HYPERKITTY_JOBS_UPDATE_INDEX_LOCKFILE.  The default is a
# file named hyperkitty-jobs-update-index.lock in the directory returned by
# tempfile.gettempdir().

# The monthly update_and_clean_index job runs for a long time and its lock can
# be broken by the hourly update_index job if it's lock lifetime is too short.
# The default is 900 seconds (15 minutes).  If the monthly job fails with
# flufl.lock._lockfile.NotLockedError: Already unlocked, increase it.
HYPERKITTY_JOBS_UPDATE_INDEX_LOCK_LIFE = 900

# Inactive List Setting
SHOW_INACTIVE_LISTS_DEFAULT = True

# Disable Posting
HYPERKITTY_ALLOW_WEB_POSTING = False


HYPERKITTY_ENABLE_GRAVATAR = True
