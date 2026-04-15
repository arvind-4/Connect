"""ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

os.environ["DJANGO_SETTINGS_MODULE"] = "backend.settings"

import django

django.setup()

from channels.auth import AuthMiddlewareStack  # noqa: E402
from channels.routing import ProtocolTypeRouter, URLRouter  # noqa: E402
from django.core.asgi import get_asgi_application  # noqa: E402

import backend.video.routing  # noqa: E402

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "https": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(backend.video.routing.websocket_urlpatterns)
        ),
    }
)
