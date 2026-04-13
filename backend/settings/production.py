import os
# import dj_database_url

from .base import *

print('Production Settings loaded')

SECRET_KEY = str(os.environ.get('SECRET_KEY'))

ADMIN_URL = str(os.environ.get('ADMIN_URL'))

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
# DATABASES['default']['ATOMIC_REQUESTS'] = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static-dev',
]

STATIC_ROOT = BASE_DIR / 'static'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ASGI_APPLICATION = 'backend.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    } 
}

LOGIN_URL = 'sign-in'

AUTH_USER_MODEL = 'backend.accounts.Account'