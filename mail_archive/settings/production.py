from settings.local import *

DEBUG = False

ALLOWED_HOSTS = ["mail-archive.mozz.us"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mail-archive/db.cnf',
            'init_command': 'SET default_storage_engine=MYISAM',
        },
    }
}

LOGGING['handlers']['file']['filename'] = "/etc/mail-archive/hyperkitty.log"
HAYSTACK_CONNECTIONS['default']['PATH'] = "/etc/mail-archive/fulltext_index"

# Security settings
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
