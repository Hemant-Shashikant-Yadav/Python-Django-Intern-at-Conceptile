"""
WSGI config for quiz_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Ensure that the settings module is set correctly
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')

# Get the WSGI application
application = get_wsgi_application()

# This may not be needed, but it ensures compatibility with WSGI-based hosting
app = application
