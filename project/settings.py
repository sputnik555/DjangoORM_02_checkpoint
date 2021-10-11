import os

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv("DATABASE_PORT"),
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': os.getenv("DATABASE_USER"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
    }
}

DEBUG = os.getenv("DEBUG")

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


