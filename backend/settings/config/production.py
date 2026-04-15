"""Production configuration settings."""
from typing import ClassVar

from backend.settings.config.base import Config, DjangoPostgresConfig, DjangoRedisConfig
from backend.utils import (
    convert_string_to_list,
    get_bool_from_env,
    get_int_from_env,
    get_string_from_env,
)


class ProductionConfig(Config):
    """Production configuration settings."""

    SECRET_KEY = get_string_from_env("DJANGO_SECRET_KEY")  # raises if unset ✓
    DEBUG = get_bool_from_env("DJANGO_DEBUG", default=False)  # safe default for prod
    ALLOWED_HOSTS = convert_string_to_list(
        value=get_string_from_env("DJANGO_ALLOWED_HOSTS")
    )
    ADMIN_URL = get_string_from_env("DJANGO_ADMIN_URL")

    POSTGRES_CONFIG: ClassVar[DjangoPostgresConfig] = {
        "DJANGO_POSTGRES_HOST": get_string_from_env("DJANGO_POSTGRES_HOST"),
        "DJANGO_POSTGRES_PORT": get_string_from_env(
            "DJANGO_POSTGRES_PORT", default="5432"
        ),
        "DJANGO_POSTGRES_USER": get_string_from_env("DJANGO_POSTGRES_USER"),
        "DJANGO_POSTGRES_PASSWORD": get_string_from_env("DJANGO_POSTGRES_PASSWORD"),
        "DJANGO_POSTGRES_DB": get_string_from_env("DJANGO_POSTGRES_DB"),
    }
    REDIS_CONFIG: ClassVar[DjangoRedisConfig] = {
        "DJANGO_REDIS_HOST": get_string_from_env(
            "DJANGO_REDIS_HOST", default="localhost"
        ),
        "DJANGO_REDIS_PORT": get_int_from_env("DJANGO_REDIS_PORT", default=6379),
    }
