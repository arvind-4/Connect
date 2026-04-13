import uuid

from .models import VideoChatRoom

def create_unique_uuid():
    new_room_id = uuid.uuid4()
    qs_room_id = VideoChatRoom.objects.filter(room_id=new_room_id)
    if qs_room_id.exists():
        room_id = uuid.uuid4()
    else:
        room_id = new_room_id
    obj = VideoChatRoom(room_id=room_id)
    obj.save()
    return room_id
    # return None