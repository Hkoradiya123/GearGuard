import os
from django.core.wsgi import get_wsgi_application

# Set default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gearguard.settings_production')

application = get_wsgi_application()
