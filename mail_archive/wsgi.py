"""
WSGI config for HyperKitty project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

try:
    from mod_wsgi import process_group
except ImportError:
    settings_module = 'settings.local'
else:
    settings_module = process_group

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
