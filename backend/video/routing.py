from django.urls import (
    re_path, 
    path
)
from django.conf import settings

from .consumers import ChatConsumer

websocket_urlpatterns = []

if settings.DEBUG:
    websocket_urlpatterns += [path('ws/<uuid:room_id>/', ChatConsumer.as_asgi())]
else:
    websocket_urlpatterns += [path('wss/<uuid:room_id>/', ChatConsumer.as_asgi())]