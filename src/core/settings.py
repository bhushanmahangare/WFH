"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b=c=w241jyszm!)l5%8_prso_&-a#4_&_q)w%q^y0xgz#z7c8^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'graphene_django',

    #User Applications
    'authentication',
    'network',
    'smartap',
    'report',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'WFH',
        'USER': 'bhushan',
        'PASSWORD': 'wifi123#',
        'HOST': 'localhost',
        #'CONN_MAX_AGE': '500',
        'OPTIONS': {
            'autocommit' : True,
            'init_command': "SET sql_mode='STRICT_ALL_TABLES'",
            'isolation_level': 'read committed',
        },
        'Test': {
            'DEPENDENCIES' : [],
        },
    },
    'smartap': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Test',
        'USER': 'bhushan',
        'PASSWORD': 'wifi123#',
        'HOST': 'localhost',
        #'CONN_MAX_AGE': 500,
        'OPTIONS': {
            'autocommit': True,
            'init_command': "SET sql_mode='STRICT_ALL_TABLES'",
            'isolation_level': 'read uncommitted',
        },
        'TEST': {
            'DEPENDENCIES': [],
        },
        #'INITIAL_SQL_FILE_PATH': '/root/wifilan.sql',
    }
}

# Database routers
DATABASE_ROUTERS = ['core.dbrouter.DBRouter']


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'




GRAPHENE = {
    'SCHEMA': 'core.schema.schema'
}

AUTH_USER_MODEL = 'authentication.AdmAccount'



AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]





# LOGGING
# https://docs.djangoproject.com/en/2.2/topics/logging/#configuring-logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'default': {
            'format': '{asctime} {levelname} {name} {message}',
            'style': '{'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'filters': [
                'require_debug_true',
            ],
            'formatter': 'default',
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/tmp/wfh-backend-debug.log',
            'filters': [
                'require_debug_true',
            ],
            'formatter': 'default',
        },
        'django': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/tmp/wfh-django.log',
            'filters': [
                'require_debug_true',
            ],
            'formatter': 'default'
        },
   },
    'loggers': {
        'django': {
            'handlers': [
                'django',
                'console',
            ],
            'level': 'DEBUG',
        },
        'authentication': {
            'handlers': [
                'debug_file',
                'console',
            ],
            'level': 'DEBUG',
        },
        'network': {
            'handlers': [
                'debug_file',
                'console',
            ],
            'level': 'DEBUG'
        },
    },
}



WIFILAN_SERVER_ID = 24
CONTROL_CENTER_URL =  "http://controlcenter.wifi-soft.com/api/remote-ap-operations.php"
WIFILAN_SERVER_AUTH_KEY = "8kaiWUJIrW";
