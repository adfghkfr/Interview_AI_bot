"""
Django settings for interview_platform project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR: 這是你的項目的根目錄。它用於構建在項目內部的其他文件或目錄的路徑。

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z%@^$%44le2bqhq#4wtq)m3)r4+ymj*0iac*pk1o=gah^do%)9'
# SECRET_KEY: 這是Django用於提供各種加密功能的秘鑰，如session cookies的簽名。在生產環境中，這個秘鑰應該保持秘密。


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG: 這是一個布爾值，用於控制是否啟用調試模式。在開發環境中，我們通常將其設置為True以便於調試。但在生產環境中，為了安全，我們應該將其設置為False。
# 允許所有主機和IP訪問你的網站

ALLOWED_HOSTS = []
# ALLOWED_HOSTS: 這是一個列表，包含了可以服務本Django應用的主機名或IP地址。在生產環境中，這個列表應該包含你的服務器的主機名或IP地址。

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]
# INSTALLED_APPS: 這是一個列表，包含了所有Django應用的名稱。Django會在這些應用中尋找模型、管理命令、測試等。

# Middleware
# 中間件是一個框架，它在Django的請求/回應處理週期中介入，執行一些任務。例如，Django提供了一個中間件來處理會話、認證等。
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 
ROOT_URLCONF = 'interview_platform.urls'

# Django模板系統
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

WSGI_APPLICATION = 'interview_platform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# 資料庫儲存設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'