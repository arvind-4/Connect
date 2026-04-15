"""Production settings for the backend project."""

from backend.infrastructure.cache.redis_cache import create_redis_cache
from backend.infrastructure.db.postgres_db import create_postgres_db
from backend.settings.base import *  # noqa: F403
from backend.settings.base import BASE_DIR
from backend.settings.config import Settings

SECRET_KEY = Settings.SECRET_KEY

ADMIN_URL = Settings.ADMIN_URL

DEBUG = Settings.DEBUG

ALLOWED_HOSTS = Settings.ALLOWED_HOSTS

DATABASES = create_postgres_db(django_postgres_config=Settings.POSTGRES_CONFIG)

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "public",
]

STATIC_ROOT = BASE_DIR / "staticfiles_build" / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles_build" / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ASGI_APPLICATION = "backend.asgi.application"
WSGI_APPLICATION = "backend.wsgi.application"

CHANNEL_LAYERS = create_redis_cache(django_redis_config=Settings.REDIS_CONFIG)

LOGIN_URL = "sign-in"

AUTH_USER_MODEL = "backend.accounts.Account"
