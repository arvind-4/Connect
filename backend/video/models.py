"""Models for the video chat room."""

import uuid

from django.db import models


class VideoChatRoom(models.Model):
    """Model for a video chat room."""

    room_id = models.UUIDField(default=uuid.uuid4, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a string representation of the video chat room."""
        return f"Room ID: {self.room_id}"
