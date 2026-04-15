"""Create a SQLite3 database."""

from backend.settings.config.base import DjangoSqliteConfig


def create_sqlite3_db(django_sqlite_config: DjangoSqliteConfig) -> None:
    """Create a SQLite3 database."""
    return {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": django_sqlite_config.get("DJANGO_SQLITE_DB"),
        }
    }
