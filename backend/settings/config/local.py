"""Local configuration settings."""
from typing import ClassVar

from backend.settings.config.base import (
    Config,
    DjangoPostgresConfig,
    DjangoRedisConfig,
    DjangoSqliteConfig,
)
from backend.utils import (
    convert_string_to_list,
    get_bool_from_env,
    get_int_from_env,
    get_string_from_env,
)


class LocalConfig(Config):
    """Local configuration settings."""

    SECRET_KEY = get_string_from_env("DJANGO_SECRET_KEY", default="insecure-secret-key")
    DEBUG = get_bool_from_env("DJANGO_DEBUG", default=True)
    ALLOWED_HOSTS = convert_string_to_list(
        value=get_string_from_env("DJANGO_ALLOWED_HOSTS", default="*")
    )

    USE_POSTGRES = get_bool_from_env("DJANGO_USE_POSTGRES", default=False)
    if USE_POSTGRES:
        POSTGRES_CONFIG: ClassVar[DjangoPostgresConfig] = {
            "DJANGO_POSTGRES_HOST": get_string_from_env(
                "DJANGO_POSTGRES_HOST", default="localhost"
            ),
            "DJANGO_POSTGRES_PORT": get_string_from_env(
                "DJANGO_POSTGRES_PORT", default="5432"
            ),
            "DJANGO_POSTGRES_USER": get_string_from_env(
                "DJANGO_POSTGRES_USER", default="postgres"
            ),
            "DJANGO_POSTGRES_PASSWORD": get_string_from_env(
                "DJANGO_POSTGRES_PASSWORD", default="postgres"
            ),
            "DJANGO_POSTGRES_DB": get_string_from_env(
                "DJANGO_POSTGRES_DB", default="postgres"
            ),
        }
    else:
        SQLITE_CONFIG: ClassVar[DjangoSqliteConfig] = {
            "DJANGO_SQLITE_DB": get_string_from_env(
                "DJANGO_SQLITE_DB", default="db.sqlite3"
            ),
        }

    USE_REDIS = get_bool_from_env("DJANGO_USE_REDIS", default=False)
    if USE_REDIS:
        REDIS_CONFIG: ClassVar[DjangoRedisConfig] = {
            "DJANGO_REDIS_HOST": get_string_from_env(
                "DJANGO_REDIS_HOST", default="localhost"
            ),
            "DJANGO_REDIS_PORT": get_int_from_env("DJANGO_REDIS_PORT", default=6379),
        }
