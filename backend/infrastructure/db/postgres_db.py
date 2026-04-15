"""Create a Postgres database."""

from backend.settings.config.base import DjangoPostgresConfig


def create_postgres_db(django_postgres_config: DjangoPostgresConfig) -> None:
    """Create a Postgres database."""
    return {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": django_postgres_config.get("DJANGO_POSTGRES_DB"),
            "HOST": django_postgres_config.get("DJANGO_POSTGRES_HOST"),
            "PORT": django_postgres_config.get("DJANGO_POSTGRES_PORT"),
            "USER": django_postgres_config.get("DJANGO_POSTGRES_USER"),
            "PASSWORD": django_postgres_config.get("DJANGO_POSTGRES_PASSWORD"),
        }
    }
