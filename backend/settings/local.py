"""Local settings for the backend project."""

from backend.infrastructure.cache.in_memory_cache import create_in_memory_cache
from backend.infrastructure.cache.redis_cache import create_redis_cache
from backend.infrastructure.db.postgres_db import create_postgres_db
from backend.infrastructure.db.sqlite3_db import create_sqlite3_db
from backend.settings.base import *  # noqa: F403
from backend.settings.base import BASE_DIR
from backend.settings.config import Settings

SECRET_KEY = Settings.SECRET_KEY

DEBUG = Settings.DEBUG

ALLOWED_HOSTS = Settings.ALLOWED_HOSTS

WSGI_APPLICATION = "backend.wsgi.application"
ASGI_APPLICATION = "backend.asgi.application"


if Settings.USE_POSTGRES:
    DATABASES = create_postgres_db(django_postgres_config=Settings.POSTGRES_CONFIG)
else:
    DATABASES = create_sqlite3_db(django_sqlite_config=Settings.SQLITE_CONFIG)


LANGUAGE_CODE = Settings.LANGUAGE_CODE

TIME_ZONE = Settings.TIME_ZONE

USE_I18N = Settings.USE_I18N

USE_TZ = Settings.USE_TZ


STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "public",
]

STATIC_ROOT = BASE_DIR / "staticfiles_build" / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles_build" / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if Settings.USE_REDIS:
    CHANNEL_LAYERS = create_redis_cache(django_redis_config=Settings.REDIS_CONFIG)
else:
    CHANNEL_LAYERS = create_in_memory_cache()

LOGIN_URL = "sign-in"

AUTH_USER_MODEL = "accounts.Account"

INTERNAL_IPS = (
    "127.0.0.1",
    "192.168.1.23",
    "localhost",
)
