"""
WSGI config for the django tree.

This exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

# IMPORTANT: use the real settings module under pwastore/config/
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pwastore.config.settings")

application = get_wsgi_application()
