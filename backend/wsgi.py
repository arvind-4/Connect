"""WSGI config for backend project."""

import os

import django
from django.core.wsgi import get_wsgi_application

django.setup()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_wsgi_application()
