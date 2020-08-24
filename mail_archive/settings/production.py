from settings.local import *

DEBUG = False

ALLOWED_HOSTS = ["mail-archive.mozz.us"]

DATABASES['default']['name'] = "/etc/mail-archive/hyperkitty.db"
LOGGING['handlers']['file']['filename'] = "/etc/mail-archive/hyperkitty.log"

# Security settings
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
