"""Utility functions for the video chat room."""

import uuid

from .models import VideoChatRoom


def create_unique_uuid() -> uuid.UUID:
    """Create a unique UUID for a video chat room."""
    new_room_id = uuid.uuid4()
    qs_room_id = VideoChatRoom.objects.filter(room_id=new_room_id)
    room_id = uuid.uuid4() if qs_room_id.exists() else new_room_id
    obj = VideoChatRoom(room_id=room_id)
    obj.save()
    return room_id
