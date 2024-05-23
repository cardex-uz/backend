"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django_application = get_asgi_application()

from .urls import ws_urlpatterns
from .authentication import WSAuthentication

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": WSAuthentication(URLRouter(ws_urlpatterns))
})
