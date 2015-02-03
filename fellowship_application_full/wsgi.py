import os
import sys

path = '/var/www/html/fellowship_application_full/'
sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fellowship_application_full.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
