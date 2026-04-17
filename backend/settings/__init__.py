"""Settings for the backend."""

import importlib

from backend.settings.base import AppEnv
from backend.utils import get_env_as_str

SETTINGS_MODULE_MAP = {
    AppEnv.DEVELOPMENT: "backend.settings.development",
    AppEnv.PRODUCTION: "backend.settings.production",
    AppEnv.TESTING: "backend.settings.testing",
}


def load_settings() -> None:
    """Load settings."""
    env_str = get_env_as_str("DJANGO_APP_ENV", default="development")
    env = AppEnv.get_app_env(env_str)

    try:
        settings_module = SETTINGS_MODULE_MAP[env]
    except KeyError:
        msg = f"Invalid DJANGO_APP_ENV: {env_str}"
        raise RuntimeError(msg) from None

    module = importlib.import_module(settings_module)
    globals().update(
        {key: value for key, value in vars(module).items() if key.isupper()}
    )


load_settings()
