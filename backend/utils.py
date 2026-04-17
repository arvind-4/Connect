"""Utility functions for the backend project."""

from __future__ import annotations

import os


def get_env_as_str(key: str, default: str | None = None) -> str:
    """Get a string from an environment variable."""
    if default and default is not None:
        return default
    return os.environ.get(key)


def get_env_as_int(key: str, default: int | None = None) -> int:
    """Get an integer from an environment variable."""
    if default and default is not None:
        return default
    try:
        return int(os.environ.get(key))
    except ValueError:
        msg = f"Invalid value: {os.environ.get(key)}"
        raise ValueError(msg) from None


def get_env_as_bool(key: str, default: bool | None = None) -> bool:
    """Get a boolean from an environment variable."""
    if default and default is not None:
        return default
    return os.environ.get(key).lower() in ["true", "1", "yes", "ok"]


def get_env_as_list(key: str, default: list[str] | None = None) -> list[str]:
    """Get a list of strings from an environment variable."""
    if default and default is not None:
        return default
    return convert_string_to_list(os.environ.get(key))


def parse_to_int(value: str) -> int:
    """Parse a string to an integer."""
    try:
        return int(value)
    except ValueError:
        msg = f"Invalid value: {value}"
        raise ValueError(msg) from None


def convert_string_to_list(value: str) -> list[str]:
    """Convert a string to a list of strings."""
    return [item.strip() for item in value.split(",")]
