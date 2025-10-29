"""
Django settings for the pwastore project (deploy-ready for Render).
"""

from pathlib import Path
import os

# -------------------- Paths --------------------
BASE_DIR = Path(__file__).resolve().parent.parent  # -> pwastore/

# -------------------- Security --------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-ky5^p#@c7fy)@105%+&5%+gv2m@(!jy+8r!&(1f6g9!l+8*om+"
)
DEBUG = os.environ.get("DEBUG", "True") == "True"
ALLOWED_HOSTS = ["*"]  # tighten in production (e.g. ['your-app.onrender.com'])

# -------------------- Apps --------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local apps (unprefixed to match your templates/models)
    "store_products.apps.StoreProductsConfig",
    "cart.apps.CartConfig",
    "accounts.apps.AccountsConfig",
    "orders.apps.OrdersConfig",
]

# -------------------- Middleware --------------------
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

# -------------------- URL/WSGI --------------------
ROOT_URLCONF = "pwastore.config.urls"
WSGI_APPLICATION = "pwastore.config.wsgi.application"

# -------------------- Templates --------------------
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
            ],
        },
    },
]

# -------------------- Database --------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -------------------- Password validation --------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------- I18N --------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -------------------- Static files --------------------
# App/third-party static collected to STATIC_ROOT on Render
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Your project-level static (where you put product images under static/products/)
STATICFILES_DIRS = [BASE_DIR / "static"]

# -------------------- Media (optional; safe to keep) --------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -------------------- Defaults --------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
