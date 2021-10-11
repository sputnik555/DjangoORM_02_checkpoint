import os
from environs import Env

ENV = Env()
ENV.read_env()

DATABASES = {
    'default': {
        'ENGINE': ENV('DATABASE_ENGINE'),
        'HOST': ENV('DATABASE_HOST'),
        'PORT': ENV("DATABASE_PORT"),
        'NAME': ENV("DATABASE_NAME"),
        'USER': ENV("DATABASE_USER"),
        'PASSWORD': ENV("DATABASE_PASSWORD"),
    }
}

DEBUG = ENV.bool("DEBUG")

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True


