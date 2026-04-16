"""Settings for the backend."""

import os

APP_ENV = os.environ.get("DJANGO_APP_ENV", "development")
if APP_ENV == "production":
    from backend.settings.production import *  # noqa: F403
elif APP_ENV == "development":
    from backend.settings.development import *  # noqa: F403
else:
    msg = f"Unknown app env: {APP_ENV}"
    raise ValueError(msg)
