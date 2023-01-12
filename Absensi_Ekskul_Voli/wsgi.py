"""
WSGI config for WebSite_Absensi_Ekskul_Voli project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebSite_Absensi_Ekskul_Voli.settings')

application = get_wsgi_application()
