"""
Django settings for Mat237 project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os, socket, math, random

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = [('Tyler', 'tholden@math.toronto.edu')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#
# SECURITY WARNING: don't run with debug turned on in production!

if socket.gethostname() == 'dobox':
    DEBUG = False
else: 
    DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1",]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_tables2',
    'Problems',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Mat237.urls'

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
                'Problems.context_processors.site_name',
            ],
        },
    },
]

WSGI_APPLICATION = 'Mat237.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if socket.gethostname() == 'dobox' or socket.gethostname() == 'TyLaptop' :
    with open('/etc/dbpasswd.txt') as f:
        dbpasswd = f.read().strip()

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'mat237db', 
            # The following settings are not used with sqlite3:
            'USER': 'tholden',
            'PASSWORD': dbpasswd,
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

if socket.gethostname() == 'dobox':
    STATIC_ROOT = "/opt/myvenv/static"
    MEDIA_ROOT  = "/opt/myvenv/media"
    NOTE_ROOT   = "/opt/myvenv/notes"
    SENDFILE_BACKEND = 'sendfile.backends.xsendfile'
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
    NOTE_ROOT   = os.path.join(BASE_DIR, 'notes')
    SENDFILE_BACKEND = 'sendfile.backends.development'

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
URL_PREPEND = ''
SITE_NAME = ''
NOTES_URL = ''

DEFAULT_FROM_ADDRESS = 'tholden@math.toronto.edu'

MEDIA_URL  = '/media/'

UNIVERSAL_CONSTANTS =  {"pi": math.pi, "e": math.e}
PREDEFINED_FUNCTIONS = {"sin": lambda x: math.sin(x),
                        "cos": lambda x: math.cos(x),
                        "tan": lambda x: math.tan(x),
                        "ln": lambda x: math.log(x, math.e),
                        "rand": lambda x,y: random.randint(x,y),
                        "uni": lambda x,y,z: round(random.uniform(x,y),z),
                        "gobble": lambda *args: 1,
                        }

try:
    from .local_settings import *
except ImportError as e:
    print('No local settings detected')
