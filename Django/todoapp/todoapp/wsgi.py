"""
WSGI config for todoapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

#from django.core.wsgi import get_wsgi_application
from configurations.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoapp.todoapp.settings')

os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')



application = get_wsgi_application()