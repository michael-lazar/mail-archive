#!/usr/bin/env python
import os
import sys


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(PROJECT_DIR)

if os.path.exists(os.path.join(PROJECT_DIR, 'PRODUCTION')):
    settings_module = 'settings.production'
else:
    settings_module = 'settings.local'


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
