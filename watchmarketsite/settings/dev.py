from watchmarketsite.settings.base import *

DEBUG = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static"),
]

MEDIA_ROOT = 'media/'