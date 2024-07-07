"""
ASGI config for project_pals project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import re_path
from chatapp.consumers import testConsumer 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_pals.settings')

application = get_asgi_application()
application = ProtocolTypeRouter({
    "websocket": 
        URLRouter([
            re_path('ws/chat/(?P<room_name>\w+)/$', testConsumer.as_asgi()),
        ])
    ,"http": get_asgi_application()
})
