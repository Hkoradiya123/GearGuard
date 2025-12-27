import os
from django.core.wsgi import get_wsgi_application

# Use production settings if available
if os.environ.get('DJANGO_SETTINGS_MODULE') is None:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gearguard.settings_production' if not os.environ.get('DEBUG', 'False').lower() == 'true' else 'gearguard.settings')

application = get_wsgi_application()
