"""
WSGI config for HyperKitty project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(PROJECT_DIR)

if os.path.exists(os.path.join(PROJECT_DIR, 'PRODUCTION')):
    settings_module = 'settings.production'
else:
    settings_module = 'settings.local'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
