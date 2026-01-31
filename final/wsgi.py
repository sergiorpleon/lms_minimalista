"""
WSGI config for final project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final.settings')

try:
    application = get_wsgi_application()
    app = application # <-- El alias para Vercel
except Exception as e:
    print(f"Error cargando la aplicacion: {e}")
    raise e
