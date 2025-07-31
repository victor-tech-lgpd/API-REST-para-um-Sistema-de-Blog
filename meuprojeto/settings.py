
# meuprojeto/settings.py
import os
from pathlib import Path

# CORREÇÃO: Importa a biblioteca 'dotenv' para carregar variáveis de ambiente
# Instale com: pip install python-dotenv
from dotenv import load_dotenv
load_dotenv() # Carrega variáveis do arquivo .env

BASE_DIR = Path(__file__).resolve().parent.parent

# CORREÇÃO: Carrega a SECRET_KEY de uma variável de ambiente. Nunca a exponha no código.
# Crie um arquivo .env na raiz do projeto e adicione: SECRET_KEY='sua-chave-gerada'
SECRET_KEY = os.getenv('SECRET_KEY', 'chave-insegura-apenas-para-dev-local')

# CORREÇÃO: O modo DEBUG nunca deve ser True em produção.
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

# CORREÇÃO: Adicione os domínios do seu site em produção aqui.
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
# Exemplo para produção: ALLOWED_HOSTS = ['.meusite.com']


# ... resto do arquivo settings.py permanece o mesmo ...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'blog',
    'api',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meuprojeto.urls'

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

WSGI_APPLICATION = 'meuprojeto.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
