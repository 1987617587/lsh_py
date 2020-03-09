"""
Django settings for wukong project.

Generated by 'django-admin startproject' using Django 3.0.4.

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
SECRET_KEY = 'y8-ae*+ikr$@v%^hfh0j0g@1^hu_q7j+*inmvu()e$mn@p-)n-'

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
    'rest_framework',
    'rentcar',
    # 'rest_framework_jwt',
    'rest_framework_simplejwt',

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

ROOT_URLCONF = 'wukong.urls'

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

WSGI_APPLICATION = 'wukong.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'media')]

# 全局配置
# 此处可以对DjangoRestFrameWork重新配置
REST_FRAMEWORK = {
    # Schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
    # # 全局配置 优先级高于视图类的配置
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.AllowAny',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',

        # # 使用JWT认证 json web token 不属于在数据库中存放 通过特殊的加密算法进行加密
        # # 配置
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        #
        # 'rest_framework.authentication.SessionAuthentication',
        # # Basic认证
        # # 将请求中携带的 类似于basic特殊编码的字符串 进行解码得到相应的用户
        # 'rest_framework.authentication.BasicAuthentication'
    ],
    #
    # # 配置全局频次限制类
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle',
    # ],
    # # Throttling
    # 'DEFAULT_THROTTLE_RATES': {
    #     'user': '500/minutes',
    #     'anon': '100/minutes',
    # },
    #
    # # Generic view behavior
    # # http://127.0.0.1:8000/categories/?limit=2&offset=1
    # # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # # http://127.0.0.1:8000/categories/?page=30
    # # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # # # Pagination
    # # 'PAGE_SIZE': 2,
    #
    # # 全局过滤
    # 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.backends.DjangoFilterBackend'],

}

AUTH_USER_MODEL = "rentcar.User"
# AUTHENTICATION_BACKENDS = ['shop.authbackend.MyLoginBackend']
#
# # from django.core.paginator import Paginator, Page
# # django分页 Paginator(分页器)  Page（每一个页）
# # DRF 提供的pageination 建立在django基础上进行深层封装
#
#
# # 允许跨域
# CORS_ORIGIN_ALLOW_ALL = True
