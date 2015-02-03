from settings_hidden import *
"""
Django settings for betterhomepage project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = hidden_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['apply.codeforprogress.org']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'widget_tweaks',
    'django_countries',
    'localflavor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fellowship_application_full.urls'

WSGI_APPLICATION = 'fellowship_application_full.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fellowship_application',
        'USER': hidden_db_user,
        'PASSWORD': hidden_db_password,
        'HOST': '127.0.0.1',
        'PORT': '5432',

    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/var/www/html/fellowship_application_full/app/static/'

STATICFILES_DIRS = (
    '/usr/lib/python2.6/site-packages/django/contrib/admin/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


    
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../app/templates/app').replace('\\','/'),
    os.path.join(os.path.dirname(__file__), '../app/templates/registration').replace('\\','/'),

)

LOGIN_URL = 'django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = 'index'

DEFAULT_FROM_EMAIL = 'aliya@codeforprogress.org'
SERVER_EMAIL = 'aliya@codeforprogress.org'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'aliya@codeforprogress.org'
EMAIL_HOST_PASSWORD = hidden_email_password
