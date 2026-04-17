"""AppConfig for the video chat room."""

from django.apps import AppConfig


class VideoConfig(AppConfig):
    """AppConfig for the video chat room."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.video"
