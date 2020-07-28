from watchmarketsite.settings.base import *

ALLOWED_HOSTS = ['*']

DEBUG = False

ADMINS = [('Bercia Catalin', 'bercia_catalin@yahoo.com')]

SERVER_EMAIL = 'bercia_catalin@yahoo.com'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django_logs.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

STATIC_ROOT = 'static/'