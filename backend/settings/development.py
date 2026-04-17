"""Local settings for the backend project."""

from backend.settings.base import *  # noqa: F403
from backend.settings.base import BASE_DIR
from backend.utils import get_env_as_bool, get_env_as_list, get_env_as_str

SECRET_KEY = get_env_as_str("DJANGO_SECRET_KEY", default="PUT_YOUR_SECRET_KEY_HERE")

DEBUG = get_env_as_bool("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = get_env_as_list("DJANGO_ALLOWED_HOSTS", default=["*"])

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
