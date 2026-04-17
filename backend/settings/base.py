"""Django settings for backend project."""

import logging
import logging.config
from enum import Enum
from pathlib import Path
from typing import Any

from backend.utils import get_env_as_str


class AppEnv(str, Enum):
    """App environment."""

    PRODUCTION = "production"
    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"

    @classmethod
    def get_app_env(cls, env: str) -> "AppEnv":
        """Get the app environment."""
        try:
            return cls(env)
        except ValueError:
            msg = f"Invalid app env: {env}"
            raise ValueError(msg) from None


class LogLevel(str, Enum):
    """Application log levels."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

    @classmethod
    def get_log_level(cls, level: str) -> "LogLevel":
        """Validate and return log level."""
        try:
            return cls(level.upper())
        except ValueError:
            msg = f"Invalid log level: {level}"
            raise ValueError(msg) from None


BASE_DIR = Path(__file__).resolve().parent.parent.parent


INSTALLED_APPS: list[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "channels",
    "backend.video",
    "backend.accounts",
]

MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


TEMPLATES: list[dict[str, Any]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ROOT_URLCONF = "backend.urls"

AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
STATIC_URL: str = "/static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


LOG_LEVEL = LogLevel.get_log_level(
    level=get_env_as_str("DJANGO_LOG_LEVEL", default="INFO")
).value
LOGGING_CONFIG = None

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "{name} at {asctime} ({levelname}) :: {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "base",
            "level": LOG_LEVEL,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": LOG_LEVEL,
    },
}

logging.config.dictConfig(LOGGING)
