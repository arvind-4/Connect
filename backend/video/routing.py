"""Routing for the video chat room."""

from django.conf import settings
from django.urls import path

from backend.video.consumers import ChatConsumer

websocket_urlpatterns = []

if settings.DEBUG:
    websocket_urlpatterns += [path("ws/<uuid:room_id>/", ChatConsumer.as_asgi())]
else:
    websocket_urlpatterns += [path("wss/<uuid:room_id>/", ChatConsumer.as_asgi())]
