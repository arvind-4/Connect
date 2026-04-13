import uuid
from django.db import models

# Create your models here.

class VideoChatRoom(models.Model):
    room_id = models.UUIDField(default=uuid.uuid4, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Room ID: {self.room_id}'