from .settings_common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
    'formatters': {
        'dev': {
           'format': '\t'.join(['%(asctime)s', '[%(levelname)s]', '%(pathname)s(Line:%(lineno)d)', '%(message)s'])
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT=os.path.join(BASE_DIR, 'media')

