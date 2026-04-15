"""Base configuration settings."""
from typing import TypedDict


class DjangoPostgresConfig(TypedDict):
    """Postgres configuration settings."""

    DJANGO_POSTGRES_HOST: str
    DJANGO_POSTGRES_PORT: str
    DJANGO_POSTGRES_USER: str
    DJANGO_POSTGRES_PASSWORD: str
    DJANGO_POSTGRES_DB: str


class DjangoSqliteConfig(TypedDict):
    """SQLite3 configuration settings."""

    DJANGO_SQLITE_DB: str


class DjangoRedisConfig(TypedDict):
    """Redis configuration settings."""

    DJANGO_REDIS_HOST: str
    DJANGO_REDIS_PORT: str


class Config:
    """Base configuration settings."""

    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "UTC"
    USE_I18N = True
    USE_TZ = True
