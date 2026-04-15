"""Create an in-memory cache."""


def create_in_memory_cache() -> None:
    """Create an in-memory cache."""
    return {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}
