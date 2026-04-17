"""Production settings for the backend project."""

from backend.settings.base import *  # noqa: F403
from backend.settings.base import BASE_DIR
from backend.utils import (
    get_env_as_bool,
    get_env_as_int,
    get_env_as_list,
    get_env_as_str,
)

SECRET_KEY = get_env_as_str("DJANGO_SECRET_KEY")

ADMIN_URL = get_env_as_str("DJANGO_ADMIN_URL")

DEBUG = get_env_as_bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = get_env_as_list("DJANGO_ALLOWED_HOSTS")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env_as_str("DJANGO_POSTGRES_DB"),
        "HOST": get_env_as_str("DJANGO_POSTGRES_HOST"),
        "PORT": get_env_as_str("DJANGO_POSTGRES_PORT"),
        "USER": get_env_as_str("DJANGO_POSTGRES_USER"),
        "PASSWORD": get_env_as_str("DJANGO_POSTGRES_PASSWORD"),
    }
}
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


STATICFILES_DIRS = [
    BASE_DIR / "public",
]

STATIC_ROOT = BASE_DIR / "staticfiles_build" / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles_build" / "media"


ASGI_APPLICATION = "backend.asgi.application"
WSGI_APPLICATION = "backend.wsgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                (
                    get_env_as_str("DJANGO_REDIS_HOST"),
                    get_env_as_int("DJANGO_REDIS_PORT"),
                )
            ],
        },
    },
}

LOGIN_URL = "sign-in"

AUTH_USER_MODEL = "accounts.Account"
