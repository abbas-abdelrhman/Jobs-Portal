# Configuration-folder/settings/_production_settings.py
# Add security related items in this file such as passwords and keys

from .settings import *
import os
import environ

env = environ.Env()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# since DEBUG is False, therefore it is compulsory to add ALLOWED_HOSTS
ALLOWED_HOSTS = ['0.0.0.0']  # add correct hostname i.e. website name

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")


# Database : Add production database details here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DATABASE_NAME"),
        'USER': env("DATABASE_USER"),
        'PASSWORD': env("DATABASE_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# production security setting

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

ADMINS = [('abbas', "gbttrial@gmail.com")]
MANAGERS = [('abbas', "gbttrial@gmail.com")]

# MIDDLEWARE += ['django.middleware.common.BrokenLinkEmailsMiddleware']

# #crispy form settings
# CRISPY_TEMPLATE_PACK = 'bootstrap5'

# #django-registration-redux settings
# ACCOUNT_ACTIVATION_DAYS=7
# REGISTRATION_AUTO_LOGIN=True
# SITE_ID=1
# LOGIN_REDIRECT_URL='/'


# SITE_HOST = 'smtp.onlinebookstore.elasticbeanstalk.com'


# # add all sites for calling API
# CORS_ORIGIN_ALLOW_ALL = True
# # #API call for specific sites
# # CORS_ORIGIN_REGEX_WHITELIST = (  ## Test these regexes somewhere - if your API won't allow AJAX calls from a whitelisted site your regexes are probably the problem
# #     r'^https?://(.+\.)?fake.co.nz',
# #     r'^https?://(.+\.)?fake.net.nz',
# # )
# # CORS_ALLOW_METHODS = (
# #     'GET',
# #     'OPTIONS',
# # )


# EMAIL_HOST_USER='gbttrial@gmail.com'
# EMAIL_HOST_PASSWORD='znhhrdibgbdnjjlm'
