from backend.settings.base import *



SECRET_KEY = 'django-insecure-e8yccf5!q5l)@upx+)tyz*=-l_1*errtn7qfm(--bj)gal4yp_'

DEBUG = True

ALLOWED_HOSTS = ['*']






WSGI_APPLICATION = 'backend.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'public',
]

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ASGI_APPLICATION = 'backend.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    } 
}

LOGIN_URL = 'sign-in'

AUTH_USER_MODEL = 'accounts.Account'

INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.1.23',
    'localhost',
)