"""Utility functions for the backend project."""

from __future__ import annotations

import os


def get_string_from_env(key: str, default: str | None = None) -> str:
    """Get a string from an environment variable."""
    if default is not None:
        return default
    value = os.environ.get(key)
    if not value:
        msg = f"Environment variable {key} is not set."
        raise ValueError(msg)
    return value


def get_bool_from_env(key: str, default: bool | None = None) -> bool:
    """Get a boolean from an environment variable."""
    if default is not None:
        return default
    value = os.environ.get(key)
    if not value:
        msg = f"Environment variable {key} is not set."
        raise ValueError(msg)
    return value.lower() in {"true", "1", "yes", "y", "ok", "okay"}


def convert_string_to_list(value: str) -> list[str]:
    """Convert a string to a list of strings."""
    return [item.strip() for item in value.split(",")]


def get_int_from_env(key: str, default: int | None = None) -> int:
    """Get a string from an environment variable."""
    if default is not None:
        return default
    value = os.environ.get(key)
    if not value:
        msg = f"Environment variable {key} is not set."
        raise ValueError(msg)
    try:
        return int(value)
    except ValueError as exc:
        msg = f"Environment variable {key} is not an integer."
        raise ValueError(msg) from exc


def get_float_from_env(key: str, default: float | None = None) -> float:
    """Get a string from an environment variable."""
    if default is not None:
        return default
    value = os.environ.get(key)
    if not value:
        msg = f"Environment variable {key} is not set."
        raise ValueError(msg)
    try:
        return float(value)
    except ValueError as exc:
        msg = f"Environment variable {key} is not a float."
        raise ValueError(msg) from exc
