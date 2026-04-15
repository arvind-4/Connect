from __future__ import annotations

from typing import TYPE_CHECKING

from backend.utils import get_string_from_env

if TYPE_CHECKING:
    from backend.settings.config.local import LocalConfig
    from backend.settings.config.production import ProductionConfig

def get_settings() -> type[LocalConfig | ProductionConfig]:
    env = get_string_from_env("APP_ENV", default="local").lower()

    if env == "production":
        from backend.settings.config.production import ProductionConfig
        return ProductionConfig
    if env == "local":
        from backend.settings.config.local import LocalConfig
        return LocalConfig

    msg = f"Invalid APP_ENV: '{env}'. Must be 'local' or 'production'."
    raise ValueError(msg) from None

Settings = get_settings()
