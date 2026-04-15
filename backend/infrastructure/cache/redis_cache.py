"""Create a Redis cache."""

from backend.settings.config.base import DjangoRedisConfig


def create_redis_cache(django_redis_config: DjangoRedisConfig) -> None:
    """Create a Redis cache."""
    return {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [(django_redis_config.get("DJANGO_REDIS_HOST"), django_redis_config.get("DJANGO_REDIS_PORT"))],
            },
        },
    }
