
import os
from pathlib import Path
from decouple import config as env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-rfjf)e6wgo&e-e&=+cj3x*3yj4rbai0-pwi9idn93t#k7#sl!m'
SECRET_KEY = env('SECRET_KEY')

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
    'django.contrib.sites',
    #
    # third party
    # "social_django",
    'django_vite',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    'django_elasticsearch_dsl',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # social
    'allauth.socialaccount.providers.google',
    #
    # custom apps
    'main',
    'blog',
    'search',
    'authentication',
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

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'esearch'
    },
}

# SOCIAL_AUTH_TRAILING_SLASH = False  # Remove trailing slash from routes
# SOCIAL_AUTH_AUTH0_DOMAIN = 'dev-11mbi3c5.us.auth0.com'
# SOCIAL_AUTH_AUTH0_KEY = 'xUvCoBcvoo6ugQ2l7G20dfYQ8mAS7T0I'
# SOCIAL_AUTH_AUTH0_SECRET = 'VeJ2zt6ZmLqikGu2m-_eUxnoR2LhbjuZssDRgangrjaiYB7aZBi_UZruEyir8cB4'

# SOCIAL_AUTH_AUTH0_SCOPE = [
#     'openid',
#     'profile',
#     'email'
# ]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('GOOGLE_AUTH_KEY'),
            'secret': env('GOOGLE_AUTH_SECRET'),
            'key': ''
        }
    }
}

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'authentication:email_confirmation_redirect'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

AUTHENTICATION_BACKENDS = {
    # 'authentication.auth0backend.Auth0',
    # 'social_core.backends.auth0.Auth0OAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
}


# LOGIN_URL = '/login/auth0/'
# LOGIN_URL = 'account_login'
LOGIN_URL = 'authentication:login_auth'
# LOGIN_REDIRECT_URL = '/'
# LOGIN_REDIRECT_URL = '/login/redirect/'
LOGIN_REDIRECT_URL = 'authentication:login_redirect'
LOGOUT_REDIRECT_URL = 'authentication:logout_redirect'
# ACCOUNT_LOGOUT_REDIRECT_URL

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_vite',
        'USER': 'root',
        'PASSWORD': 'root',
        # 'HOST': '127.0.0.1',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

DJANGO_VITE_ASSETS_PATH = BASE_DIR / "static" / "dist"

STATIC_ROOT = 'collectedstaticfiles'


STATICFILES_DIRS = [
    DJANGO_VITE_ASSETS_PATH,
    # os.path.join(DJANGO_VITE_ASSETS_PATH, "dist"),
    os.path.join(BASE_DIR, "static/src"),
    os.path.join(BASE_DIR, "media/")
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

DJANGO_VITE_DEV_MODE = DEBUG

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "ck-uploads/"

# CKEDITOR_CONFIGS = {
#     "default": {
#         'skin': 'moono_dark',
#     }
# }

CKEDITOR_ALLOW_NONIMAGE_FILES = False
