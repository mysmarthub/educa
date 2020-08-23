from myeduca.settings.base import *


DEBUG = False


ADMINS = (
    ('', ''),
)
ALLOWED_HOSTS = ['myeducaproject.com', 'www.myeducaproject.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
