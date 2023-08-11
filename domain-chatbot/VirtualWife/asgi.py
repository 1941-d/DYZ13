"""
ASGI config for VirtualWife project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""


import os
import apps.chatbot.bulletscreen.core.bili_schedule
from apps.chatbot.bulletscreen.routing import websocket_urlpatterns
from apps.chatbot.bulletscreen.core.zblivedm_main import start_handle
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VirtualWife.settings')

start_handle();

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
})

