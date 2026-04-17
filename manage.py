"""Django's command-line utility for administrative tasks."""

import logging
import os
import sys
from pathlib import Path

from django.core.management import execute_from_command_line

logger = logging.getLogger(__name__)


try:
    from dotenv import load_dotenv
except ImportError:
    msg = (
        "Error while importing dotenv. Did you forget to install it?"
        "Run `uv sync` to sync the dependencies."
        "or run `uv add --dev  python-dotenv` to add it."
    )
    logger.exception(msg)


BASE_DIR = Path(__file__).resolve(strict=True).parent

env_files: list[str] = [
    ".env",
]

for env_file in env_files:
    env_path = BASE_DIR / env_file
    if env_path.exists():
        load_dotenv(env_path)


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        msg = (
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
        raise ImportError(msg) from exc


if __name__ == "__main__":
    main()
