"""
WSGI config for magazin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys


path = '/home/dmitrygorbachev/magazanywhere/magazin'  # use your own PythonAnywhere username here
if path not in sys.path:
    sys.path.append(path)
from django.core.wsgi import get_wsgi_application

os.environ["SECRET_KEY"] = "d5+*iszxz-rel-1td0rz8*(bjj2&j!==i*)d0pp69au^x23v)&"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "magazin.deploy_settings")




from whitenoise.django import DjangoWhiteNoise


application = get_wsgi_application()
application = DjangoWhiteNoise(application)
