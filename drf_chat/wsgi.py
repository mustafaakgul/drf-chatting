"""
WSGI config for drf_chat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# configuration = os.getenv('ENVIRONMENT', 'development').title()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_chat.settings")

application = get_wsgi_application()
