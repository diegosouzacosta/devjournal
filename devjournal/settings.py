# -*- coding: utf8 -*-
# vim: ts=4 sts=4 sw=4 et:

import sys
from os import path

import dj_database_url
from decouple import undefined, config as decouple


if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")


def megabytes(mb):
    return mb * (1024 ** 2)


def one_or_true(text):
    return text == '1' or text == 'True'


def config(key, default=undefined, cast=undefined):
    if DEBUG and default is undefined:
        default = ''

    return decouple(key, default=default, cast=cast)


DEBUG = decouple('DEBUG', default=False, cast=one_or_true)
SECRET_KEY = decouple('SECRET_KEY')

VERSION = '0.0.1'

ALLOWED_HOSTS = ['*']
WSGI_APPLICATION = 'devjournal.wsgi.application'
ROOT_URLCONF = 'devjournal.urls'
LANGUAGE_CODE = 'en-US'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'devjournal',
    'rest_framework',
    'journal',
    'webhooks',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'devjournal.urls'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination'
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': dj_database_url.config(default=decouple('DATABASE_DEFAULT')),
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-spec',
    '--spec-color',
    '--with-coverage',
    '--cover-erase',
    '--cover-html',
    '--cover-branches',
    '--cover-package=web,payment,new_user',
]

if DEBUG:
    LOG_DIR = path.dirname(path.abspath(__file__)) + '/log/'
else:
    LOG_DIR = '/var/log/devjournal'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '[{}] %(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'.format(VERSION)
        },
        'tracing': {
            'format': (
                '[{}] %(CONNECTION)s;%(CONNECTION_REQUESTS)s;%(process)d;%(threadName)s;'
                '%(filename)s:%(funcName)s[%(lineno)d];%(asctime)s;%(duration)f;%(sql)s;%(params)s'.format(VERSION)
            )
        },
        'simple': {
            'format': '[{}] %(asctime)s %(levelname)s %(message)s'.format(VERSION)
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'environ': {'()': type('null_filter', (), {'filter': (lambda self, record: False)})},
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['require_debug_false'],
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['require_debug_true'],
        },
        'tracing': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(LOG_DIR, 'tracing.log'),
            'maxBytes': megabytes(10),
            'backupCount': 2,
            'formatter': 'tracing',
            'filters': ['environ'],
        },
        'commands': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(LOG_DIR, 'commands.log'),
            'maxBytes': megabytes(10),
            'backupCount': 2,
            'formatter': 'simple',
            'filters': ['require_debug_false'],
        },
        'commands_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(LOG_DIR, 'commands.log'),
            'maxBytes': megabytes(10),
            'backupCount': 2,
            'formatter': 'simple',
            'filters': ['require_debug_true'],
        },
        'historical': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(LOG_DIR, 'historical.log'),
            'maxBytes': megabytes(10),
            'backupCount': 2,
            'formatter': '',
            'filters': ['environ'],
        },
        'null': {
            'class': 'django.utils.log.NullHandler',
        }
    },
    'root': {
        'handlers': ['console', 'debug'],
    },
    'loggers': {
        'django.db.backends.schema': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['tracing'],
            'propagate': False,
        },
        'nose': {
            'handlers': ['null'],
            'propagate': False
        },
        'urllib3': {
            'handlers': ['null'],
            'propagate': False
        },
        'commands': {
            'level': 'DEBUG',
            'handlers': ['commands', 'commands_debug'],
            'propagate': False,
        },
        'historical': {
            'level': 'INFO',
            'handlers': ['historical'],
            'propagate': False,
        },
        'django': {},
    }
}

if DEBUG:
    LOGGING['root']['level'] = 'DEBUG'
    LOGGING['loggers']['spyne'] = {
        'handlers': [],
        'propagate': False,
    }
