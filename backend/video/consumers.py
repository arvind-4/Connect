"""WebSocket consumer for the video chat room."""

import json
from typing import Any

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """WebSocket consumer for the video chat room."""

    async def connect(self) -> None:
        """Join the video chat room."""
        self.room_name = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"Video-Chat-{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(
        self, *_args: tuple[Any, ...], **_kwargs: dict[str, Any]
    ) -> None:
        """Remove the video chat room from the group."""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data: str) -> None:
        """Receive an SDP message from the video chat room."""
        receive_dict = json.loads(text_data)
        action = receive_dict["action"]
        if action in {"new-offer", "new-answer"}:
            receiver_channel_name = receive_dict["message"]["receiver_channel_name"]
            receive_dict["message"]["receiver_channel_name"] = self.channel_name
            await self.channel_layer.send(
                receiver_channel_name,
                {
                    "type": "send.sdp",
                    "receive_dict": receive_dict,
                },
            )
            return
        receive_dict["message"]["receiver_channel_name"] = self.channel_name
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send.sdp",
                "receive_dict": receive_dict,
            },
        )

    async def send_sdp(self, event: dict[str, Any]) -> None:
        """Send an SDP message to the video chat room."""
        receive_dict = event["receive_dict"]
        this_peer = receive_dict["peer"]
        action = receive_dict["action"]
        message = receive_dict["message"]

        await self.send(
            text_data=json.dumps(
                {
                    "peer": this_peer,
                    "action": action,
                    "message": message,
                }
            )
        )
