import os
from django.core.asgi import get_asgi_application

# Set default settings module to production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gearguard.settings_production')

application = get_asgi_application()
