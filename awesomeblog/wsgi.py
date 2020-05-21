import os
from dj_static import Cling #heroku config

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'awesomeblog.settings')

application = Cling(get_wsgi_application()) #heroku config
