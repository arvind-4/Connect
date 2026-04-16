"""Local settings for the backend project."""

import os

from backend.settings.base import *  # noqa: F403
from backend.settings.base import BASE_DIR

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") or "12"

DEBUG = os.environ.get("DJANGO_DEBUG") or True

ALLOWED_HOSTS = ["*"]


WSGI_APPLICATION = "backend.wsgi.application"
ASGI_APPLICATION = "backend.asgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


STATICFILES_DIRS = [
    BASE_DIR / "public",
]

STATIC_ROOT = BASE_DIR / "staticfiles_build" / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles_build" / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}

LOGIN_URL = "sign-in"

AUTH_USER_MODEL = "accounts.Account"

INTERNAL_IPS = (
    "127.0.0.1",
    "192.168.1.23",
    "localhost",
)
