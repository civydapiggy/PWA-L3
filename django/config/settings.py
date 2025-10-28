"""
Django settings for the 'pwastore' project package.
Works locally and on Render (or similar) with Whitenoise static serving.
"""

from pathlib import Path
import os

# -------------------------
# Paths
# -------------------------
# BASE_DIR points to the pwastore/ folder (parent of config/)
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# Security
# -------------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-7#9wyx$f5h6jt4*4i&xk^loxjm7h9d#ydq6df!4zj7r+#bl2bb"
)
DEBUG = os.environ.get("DEBUG", "True") == "True"
ALLOWED_HOSTS = ["*"]  # tighten in production

# -------------------------
# Applications
# -------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local apps
    "store_products",
    "cart",
    "accounts",
    "orders.apps.OrdersConfig",
]

# -------------------------
# Middleware
# -------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # serve static files in prod
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Use the pwastore.config.* modules
ROOT_URLCONF = "pwastore.config.urls"
WSGI_APPLICATION = "pwastore.config.wsgi.application"

# -------------------------
# Templates
# -------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # pwastore/templates/
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "store_products.context_processors.category_links",
            ],
        },
    },
]

# -------------------------
# Database (SQLite)
# -------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -------------------------
# Password validation
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------
# Internationalization
# -------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -------------------------
# Static files
# -------------------------
STATIC_URL = "/static/"

# Allow env override (Render) but default to pwastore/staticfiles
STATIC_ROOT = os.environ.get("STATIC_ROOT", str(BASE_DIR / "staticfiles"))

# Whitenoise compressed, cache-busting storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -------------------------
# Defaults
# -------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
