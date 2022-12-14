"""
Django settings for upload_json project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m2q_z9vo-vvyi@cek8(v*(k7r9n99)0*twv5r1op-s%i5o*1n='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'login',
    'filesUpload',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'drf_yasg.middleware.SwaggerExceptionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'upload_json.urls'

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

WSGI_APPLICATION = 'upload_json.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '0.0.0.0',
        'NAME': 'upload_json',
        'USER': 'root',
        'PASSWORD': 'Hobasa@7',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_URL = r'/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, os.path.join('static', 'files')),
]

# Testing
TEST_RUNNER = 'upload_json.runner.PytestTestRunner'

U_LOGFILE_NAME = os.path.join(BASE_DIR, 'Logging.log')
U_LOGFILE_SIZE = 5 * 1024 * 1024
U_LOGFILE_COUNT = 3
# U_LOGFILE_APP1 = 'app1'
# U_LOGFILE_APP2 = 'app2'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(levelname)7s | %(name)10s | %(filename)15s:%(lineno)4d -%(funcName)8s %(asctime)s, %(msecs)s, %(message)s'
        },
        'pipe_separated': {
            'format': '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console_log': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'pipe_separated',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': U_LOGFILE_NAME,
            'maxBytes': U_LOGFILE_SIZE,
            'backupCount': U_LOGFILE_COUNT,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'drf_yasg': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': True,
        },
        'swagger_spec_validator': {
            'handlers': ['console_log'],
            'level': 'INFO',
            'propagate': False,
        }
    },
    'root': {
        'handlers': ['console_log'],
        'level': 'INFO',
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SWAGGER_SETTINGS = {
    "BASE_PATH": '/api/v1/',

    'DEFAULT_INFO': 'upload_json.urls.swagger_info',

    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        },
        'Bearer': {
            'in': 'header',
            'name': 'Authorization',
            'type': 'apiKey',
        },
        # 'OAuth2 password': {
        #     'flow': 'password',
        #     'scopes': {
        #         'read': 'Read everything.',
        #         'write': 'Write everything,',
        #     },
        #     'tokenUrl': OAUTH2_TOKEN_URL,
        #     'type': 'oauth2',
        # },
        'Query': {
            'in': 'query',
            'name': 'auth',
            'type': 'apiKey',
        },
    },
    "DEFAULT_PAGINATOR_INSPECTORS": [
        'drf_yasg.inspectors.DjangoRestResponsePagination',
        'drf_yasg.inspectors.CoreAPICompatInspector',
    ]
}

REDOC_SETTINGS = {
    'SPEC_URL': ('schema-json', {'format': '.json'}),
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', )
}