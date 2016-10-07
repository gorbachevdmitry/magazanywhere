from ..settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'localhost',
    '.pythonanywhere.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shoppythonanywhere',
        'USER': 'dmitrygorbachev',
        'PASSWORD': '150881',
        'HOST': '.pythonanywhere.com',
        'PORT': '',
    }
}