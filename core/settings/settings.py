
import os
from pathlib import Path
from decouple import config as env
from corsheaders.defaults import default_headers
# from core.settings import AWS_S3_CUSTOM_DOMAIN
from urllib.parse import quote_plus as urlquote


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env('DEBUG', default=False, cast=bool)
DEBUG = env('DEBUG', cast=bool)

SITE_NAME = env('VITE_WEBSITE_NAME')
SITE_ORIGIN = env('VITE_WEBSITE_ORIGIN')

ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "https://oauth2.googleapis.com",
    # "https://www.googleapis.com",
    "https://accounts.google.com",
    'https://djangovite.s3.amazonaws.com'
]
# CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "https://oauth2.googleapis.com",
    "https://accounts.google.com",
    'https://djangovite.s3.amazonaws.com'

    #     # "https://www.googleapis.com"
]

# CORS_ALLOW_HEADERS = [
#     "accept",
#     "accept-encoding",
#     "authorization",
#     "content-type",
#     "dnt",
#     "origin",
#     "user-agent",
#     "x-csrftoken",
#     "x-requested-with",
# ]
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
    "storages",
    "corsheaders",
    'django_vite',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'dj_rest_auth',
    'dj_rest_auth.registration',
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
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': f'https://{env("AWS_ELASTICSEARCH_USER")}:{env("AWS_ELASTICSEARCH_PASSWORD")}@search-dv-es-domain-edbqiwgdai4m6nchjyv5f67ztu.us-east-1.es.amazonaws.com'
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
SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('VITE_GOOGLE_AUTH_KEY'),
            'secret': env('VITE_GOOGLE_AUTH_SECRETE'),
            'key': ''
        }
    }
}

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'authentication:email_confirmation_redirect'
ACCOUNT_FORMS = {'signup': 'authentication.forms.CustomSignupForm'}
# ACCOUNT_ADAPTER = 'authentication.adapter.CustomAccountAdapter'

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

REST_USE_JWT = True

JWT_AUTH_COOKIE = env('VITE_JWT_AUTH_COOKIE')
JWT_AUTH_REFRESH_COOKIE = env('VITE_JWT_AUTH_REFRESH_COOKIE')

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
        # 'DIRS': [],
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
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT', cast=int),
    }
}


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

# DJANGO_VITE_ASSETS_PATH = BASE_DIR / "static" / "dist"

STATIC_ROOT = 'collectedstaticfiles'


# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

AWS_S3_ACCESS_KEY_ID = env('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = env('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = 'public-read'


AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}

# AWS_LOCATION = STATIC_ROOT
AWS_LOCATION = 'collectedstaticfiles'
# AWS_LOCATION = DJANGO_VITE_ASSETS_PATH

# STATIC_URL = '/static/'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'

# DJANGO_VITE_ASSETS_PATH = STATIC_URL
DJANGO_VITE_ASSETS_PATH = BASE_DIR / "static" / "dist"


STATICFILES_DIRS = [
    DJANGO_VITE_ASSETS_PATH,
]

DEFAULT_FILE_STORAGE = 'core.storages.MediaStorage'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/media/'
# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
# MEDIA_ROOT = os.path.join(BASE_DIR, "collectedstaticfiles/")

DJANGO_VITE_DEV_MODE = False

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


GOOGLE_OAUTH2_CALLBACK_URL = f'{env("VITE_WEBSITE_PROTOCOL")}{env("VITE_WEBSITE_PROTOCOL_HEAD")}{env("VITE_WEBSITE_DOMAIN")}'
