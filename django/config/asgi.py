"""
ASGI config for the project.

This exposes the ASGI callable as a module-level variable named ``application``.
"""

import os
from django.core.asgi import get_asgi_application

# IMPORTANT: point to the correct settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pwastore.config.settings")

application = get_asgi_application()
