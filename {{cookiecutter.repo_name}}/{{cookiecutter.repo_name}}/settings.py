from os import path

from environ import Path, Env

# Django-environ basics
root = Path(__file__) - 2
env = Env(DEBUG=(bool, False),)

# Read a file with environment variables, these variables can be used to set the value of django settings
ENV_FILE = str(env.path('ENV_FILE', default='.env'))
if path.isfile(ENV_FILE):
    Env.read_env(ENV_FILE)
else:
    # unset if no file was found
    ENV_FILE = None

# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = root()

# Django Debug option
DEBUG = env.bool('DEBUG')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='xt515nl958u+8sbk_e($p%g_$olz9)!y)8+snv*yhsk1!hm(_c')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # shell plus
    'django_extensions',

    # Django REST framework
    'rest_framework',

    # django parler
    'parler',
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

ROOT_URLCONF = '{{cookiecutter.repo_name}}.urls'

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

WSGI_APPLICATION = '{{cookiecutter.repo_name}}.wsgi.application'


# Database
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite://:memory:'),
}

# Password validation
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

# parler: have translations active by default
PARLER_DEFAULT_ACTIVATE = True
