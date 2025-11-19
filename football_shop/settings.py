"""
Django settings for football_shop project.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-d6x7y=3aw^5!qn&x(*4vyjyldqlg3%iw#114n@tix5jg))f2jh"
)

PRODUCTION = os.getenv("PRODUCTION", "False").lower() == "true"

DEBUG = True

# ALLOWED_HOSTS - PENTING untuk Flutter!
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "10.0.2.2",  # Android Emulator
    "faishal-khoiriansyah-footballshop.pbp.cs.ui.ac.id",
]

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    "https://faishal-khoiriansyah-footballshop.pbp.cs.ui.ac.id",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://10.0.2.2:8000",
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'corsheaders',  # TAMBAHKAN INI
    'main',
    'authentication',  # TAMBAHKAN INI
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # TAMBAHKAN INI - HARUS SEBELUM CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS Configuration - PENTING untuk Flutter!
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://10.0.2.2:8000",
]

# Cookie Settings untuk Cross-Origin
CSRF_COOKIE_SECURE = False  # Set True di production dengan HTTPS
SESSION_COOKIE_SECURE = False  # Set True di production dengan HTTPS
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'

# Untuk development
if not PRODUCTION:
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SAMESITE = 'Lax'

ROOT_URLCONF = 'football_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'football_shop.wsgi.application'

# Database
if PRODUCTION:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            'OPTIONS': {
                'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
            }
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'