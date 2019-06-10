"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ipr*&g+talkmr6=cl2e82cp-%==9cpbvo!ny6bc2p398_h5d%m'

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
    'debug_toolbar',
    'shop',  # 제품, 카테고리
    'cart',  # 장바구니 - 세션 방식(소유자를 매칭할 필요가 없다), 데이터베이스 방식
    'coupon',  # 할인 - 금액, 퍼센트할인, 무료 제품, 무료 배송
    'order',  # 실제 주문 - 주문 후 배송조회, invoice 확인, iamport 결제
    'django_summernote',
    'ckeditor',
    'ckeditor_uploader',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'layout')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


# 1. PostgreSQL - 마스터 / 슬레이브1
# 2. 라우터 설정
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop_master',
        'USER': 'sug5806',
        'PASSWORD': 'ghd941322',
        'HOST': 'shop.cakloest4jdx.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    },
    'read1': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop_master',
        'USER': 'sug5806',
        'PASSWORD': 'ghd941322',
        'HOST': 'shop-slave.cakloest4jdx.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }

}

DATABASE_ROUTERS = ['config.master_slave_router.MasterSlaveRouter']

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 's-shop'

AWS_S3_CUSTOM_DOMAIN = 's3.%s.amazonaws.com/%s' % (AWS_REGION, AWS_STORAGE_BUCKET_NAME)
AWS_S3_FILE_OVERWRITE = False



AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl' : 'max-age=86400',
}

AWS_S3_SECURE_URLS = False


AWS_DEFAULT_ACT = 'public-read'
AWS_LOCATION = ''

DEFAULT_FILE_STORAGE = 'config.s3media.MediaStorage'


STATIC_URL = 'http://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_UPLOAD_PATH = 'wysiwyg/'



# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


# s3 - Media, Static 서버 별도로(도메인X)
STATIC_URL = '/static/'

INTERNAL_IPS = ['127.0.0.1']
