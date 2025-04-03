# ruff: noqa: ERA001, E501
"""Base settings to build other settings files upon."""
import re
{%- if cookiecutter.use_simplejwt == "y" %}
from datetime import timedelta
{%- endif %}

{% if cookiecutter.use_celery == 'y' -%}
import ssl
{%- endif %}
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# {{ cookiecutter.project_slug }}/
APPS_DIR = BASE_DIR / "{{ cookiecutter.project_slug }}"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(BASE_DIR / ".env"))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "{{ cookiecutter.timezone }}"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#languages
# from django.utils.translation import gettext_lazy as _
# LANGUAGES = [
#     ('en', _('English')),
#     ('fr-fr', _('French')),
#     ('pt-br', _('Portuguese')),
# ]
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(BASE_DIR / "locale")]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
{% if cookiecutter.use_docker == "y" -%}
DATABASES = {"default": env.db("DATABASE_URL")}
{%- else %}
DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default="postgres://{% if cookiecutter.windows == 'y' %}localhost{% endif %}/{{cookiecutter.project_slug}}",
    ),
}
{%- endif %}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    # "{{ cookiecutter.project_slug }}.admin.apps.CustomAdminConfig",  # Custom admin
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.mfa",
    "allauth.socialaccount",
    # "allauth.socialaccount.providers.facebook",
    # "allauth.socialaccount.providers.google",
{%- if cookiecutter.use_celery == 'y' %}
    "django_celery_beat",
{%- endif %}
{%- if cookiecutter.use_drf == "y" %}
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_spectacular",
{%- endif %}
{%- if cookiecutter.frontend_pipeline == 'Webpack' %}
    "webpack_loader",
{%- endif %}
    # Forked additions
{%- if cookiecutter.use_dj_rest_auth == "y" %}
    "dj_rest_auth",
{%- endif %}
{%- if cookiecutter.use_simplejwt == "y" %}
    "rest_framework_simplejwt",
{%- endif %}
{%- if cookiecutter.use_celery == 'y' %}
    "django_celery_results",
{%- endif %}
{%- if cookiecutter.use_oauth == "y" %}
    "oauth2_provider",
{%- endif %}
    "django_perm_filter",
{%- if cookiecutter.use_robots == "y" %}
    "robots",
{%- endif %}
{%- if cookiecutter.use_django_auditlog == "y" %}
    "auditlog",
{%- endif %}
{%- if cookiecutter.use_drf_api_logger == "y" %}
    "drf_api_logger",
{%- endif %}
    "widget_tweaks",
]

LOCAL_APPS = [
    "{{ cookiecutter.project_slug }}.users",
    # Your stuff: custom apps go here
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "{{ cookiecutter.project_slug }}.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
{%- if cookiecutter.use_drf == 'y' %}
    "corsheaders.middleware.CorsMiddleware",
{%- endif %}
{%- if cookiecutter.use_whitenoise == 'y' %}
    "whitenoise.middleware.WhiteNoiseMiddleware",
{%- endif %}
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
{%- if cookiecutter.use_oauth == 'y' %}
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
{%- endif %}
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
{%- if cookiecutter.use_drf_api_logger == "y" %}
    "drf_api_logger.middleware.api_logger_middleware.APILoggerMiddleware",
{%- endif %}
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(BASE_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(BASE_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": [str(APPS_DIR / "templates")],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "{{ cookiecutter.project_slug }}.users.context_processors.allauth_settings",
                "{{ cookiecutter.project_slug }}.utils.context_processors.settings_context",
            ],
        },
    },
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""{{cookiecutter.author_name}}""", "{{cookiecutter.email}}")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# https://cookiecutter-django.readthedocs.io/en/latest/settings.html#other-environment-settings
# Force the `admin` sign in process to go through the `django-allauth` workflow
DJANGO_ADMIN_FORCE_ALLAUTH = env.bool("DJANGO_ADMIN_FORCE_ALLAUTH", default=False)

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
        "custom_formatter": {
            "format": "[%(levelname)s] %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
            "datefmt": "%Y-%m-%d %I:%M:%S %p",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            # "formatter": "verbose",
            "formatter": "custom_formatter",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    # "loggers": {
    #     "django.db.backends": {
    #         "level": "WARNING",
    #         "handlers": ["console"],
    #         "propagate": False,
    #     },
    #     "django.request": {
    #         "handlers": ["console"],
    #         "level": "ERROR",
    #         "propagate": False,
    #     },
    #     "django.server": {
    #         "level": "WARNING",
    #         "handlers": ["console"],
    #         "propagate": False,
    #     },
    #     "{{ cookiecutter.project_slug }}": {
    #         "level": "DEBUG",
    #         "handlers": ["console"],
    #         "propagate": False,
    #     },
    # },
}

REDIS_URL = env("REDIS_URL", default="redis://{% if cookiecutter.use_docker == 'y' %}redis{%else%}localhost{% endif %}:6379/0")
REDIS_SSL = REDIS_URL.startswith("rediss://")

{% if cookiecutter.use_celery == 'y' -%}
# Celery
# ------------------------------------------------------------------------------
if USE_TZ:
    # https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-timezone
    CELERY_TIMEZONE = TIME_ZONE
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = REDIS_URL
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#redis-backend-use-ssl
CELERY_BROKER_USE_SSL = {"ssl_cert_reqs": ssl.CERT_NONE} if REDIS_SSL else None
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-result_backend
CELERY_RESULT_BACKEND = REDIS_URL
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#redis-backend-use-ssl
CELERY_REDIS_BACKEND_USE_SSL = CELERY_BROKER_USE_SSL
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#result-extended
CELERY_RESULT_EXTENDED = True
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#result-backend-always-retry
# https://github.com/celery/celery/pull/6122
CELERY_RESULT_BACKEND_ALWAYS_RETRY = True
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#result-backend-max-retries
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ["json"]
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = "json"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = "json"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_TIME_LIMIT = 5 * 60
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 60
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#beat-scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#worker-send-task-events
CELERY_WORKER_SEND_TASK_EVENTS = True
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-task_send_sent_event
CELERY_TASK_SEND_SENT_EVENT = True
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#worker-hijack-root-logger
CELERY_WORKER_HIJACK_ROOT_LOGGER = False

# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
CELERY_RESULT_BACKEND = "django-db"
# CELERY_RESULT_BACKEND = env("CELERY_BROKER_URL")

{%- endif %}
# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://docs.allauth.org/en/latest/account/configuration.html
ACCOUNT_LOGIN_METHODS = {"{{cookiecutter.username_type}}"}
# https://docs.allauth.org/en/latest/account/configuration.html
{%- if cookiecutter.username_type == "username" %}
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]
{%- else %}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
# https://docs.allauth.org/en/latest/account/configuration.html
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
{%- endif %}
# https://docs.allauth.org/en/latest/account/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# https://docs.allauth.org/en/latest/account/configuration.html
ACCOUNT_ADAPTER = "{{cookiecutter.project_slug}}.users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
ACCOUNT_FORMS = {"signup": "{{cookiecutter.project_slug}}.users.forms.UserSignupForm"}
# https://docs.allauth.org/en/latest/socialaccount/configuration.html
SOCIALACCOUNT_ADAPTER = "{{cookiecutter.project_slug}}.users.adapters.SocialAccountAdapter"
# https://docs.allauth.org/en/latest/socialaccount/configuration.html
SOCIALACCOUNT_FORMS = {"signup": "{{cookiecutter.project_slug}}.users.forms.UserSocialSignupForm"}
{% if cookiecutter.frontend_pipeline == 'Django Compressor' -%}
# django-compressor
# ------------------------------------------------------------------------------
# https://django-compressor.readthedocs.io/en/latest/quickstart/#installation
INSTALLED_APPS += ["compressor"]
STATICFILES_FINDERS += ["compressor.finders.CompressorFinder"]
{%- endif %}
{% if cookiecutter.use_drf == "y" -%}
# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["{{cookiecutter.project_slug}}.api.renderers.MyJSONRenderer"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        {% if cookiecutter.use_oauth == "y" -%}
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        {%- endif %}
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        {%- if cookiecutter.use_simplejwt == "y" %}
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        {%- endif %}
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"
# CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    env.list("CORS_ORIGIN_WHITELIST", default=["http://localhost:8080", "http://localhost:8000"])
)

# By Default swagger ui is available only to admin user(s). You can change permission classes to change that
# See more configuration options at https://drf-spectacular.readthedocs.io/en/latest/settings.html#settings
SPECTACULAR_SETTINGS = {
    "TITLE": "{{ cookiecutter.project_name }} API",
    "DESCRIPTION": "Documentation of API endpoints of {{ cookiecutter.project_name }}",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "SERVERS": [
        {"url": "http://127.0.0.1:8000", "description": "Local Development server"},
        {"url": "https://{{ cookiecutter.domain_name }}", "description": "Production server"},
    ],
    "SCHEMA_PATH_PREFIX": r"/api/v[0-9]",
}
{%- endif %}

{%- if cookiecutter.frontend_pipeline == 'Webpack' %}
# django-webpack-loader
# ------------------------------------------------------------------------------
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "STATS_FILE": BASE_DIR / "webpack-stats.json",
        "POLL_INTERVAL": 0.1,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    },
}

{%- endif %}

# ------------------------------------------------------------------------------
# FORKED ADDITIONS - keeps diffs minimal
# ------------------------------------------------------------------------------
{%- if cookiecutter.use_dj_rest_auth == "y" %}
# dj-rest-auth https://dj-rest-auth.readthedocs.io/en/latest/configuration.html
# -------------------------------------------------------------------------------
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
    # "USER_DETAILS_SERIALIZER": "django_spaday.api.serializers.UserAuthSerializer",
}
{%- endif %}

{%- if cookiecutter.use_simplejwt == "y" %}
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.htm
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "UPDATE_LAST_LOGIN": True,
}
{%- endif %}

# CSRF
# ------------------------------------------------------------------------------
# CSRF_COOKIE_SAMESITE = 'Strict'
# CSRF_COOKIE_HTTPONLY = False  # False if using django-spaday
CSRF_TRUSTED_ORIGINS=env.list("CSRF_TRUSTED_ORIGINS", default=["http://localhost:8081", "http://localhost:8000"])

# Session
# ------------------------------------------------------------------------------
SESSION_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_AGE = 60 * 60 * 8  # 8 hrs

{%- if cookiecutter.use_oauth == "y" %}
OAUTH2_PROVIDER = {
    "ACCESS_TOKEN_EXPIRE_SECONDS": 60 * 60 * 8,
    "REFRESH_TOKEN_EXPIRE_SECONDS": 60 * 60 * 8,
    # this is the list of available scopes
    "SCOPES": {
        "example:read": "Example read scope",
        "example:write": "Example write scope",
    },
}
{%- endif %}

{%- if cookiecutter.use_robots == "y" %}
# django-robots - # https://django-robots.readthedocs.io/en/latest/
# ------------------------------------------------------------------------------
ROBOTS_USE_SITEMAP = False
ROBOTS_USE_HOST = True
ROBOTS_USE_SCHEME_IN_HOST = True
# ROBOTS_CACHE_TIMEOUT = 60 * 60 * 24  # 24 hours
{%- endif %}

{%- if cookiecutter.use_perm_filter == 'y' %}
# django-perm-filter
# -------------------------------------------------------------------------------
PERM_FILTER = {
    "USER_ADMIN": "{{ cookiecutter.project_slug }}.users.admin.UserAdmin",
    "HIDE_PERMS": [
        # Django built-ins
        "admin",
        "contenttypes",
        "sessions",
        "sites",
        # Auditlog
        "auditlog.add_logentry",
        "auditlog.change_logentry",
        "auditlog.delete_logentry",
        # All-auth
        "account",
        "socialaccount",
        {%- if cookiecutter.use_celery == "y" %}
        # Celery
        "django_celery_beat",
        "django_celery_results",
        {%- endif %}
        "thumbnail",
        # Django built-in auth permissions
        "auth.view_permission",
        "auth.add_permission",
        "auth.change_permission",
        "auth.delete_permission",
        # Authtoken Token/TokenProxy
        "authtoken.view_token",
        "authtoken.add_token",
        "authtoken.change_token",
        "authtoken.delete_token",
        "authtoken.view_tokenproxy",
        "authtoken.add_tokenproxy",
        "authtoken.change_tokenproxy",
        "authtoken.delete_tokenproxy",
        {%- if cookiecutter.use_oauth == "y" %}
        # oAuth2
        "oauth2_provider.view_idtoken",
        "oauth2_provider.add_idtoken",
        "oauth2_provider.change_idtoken",
        "oauth2_provider.delete_idtoken",
        "oauth2_provider.view_grant",
        "oauth2_provider.add_grant",
        "oauth2_provider.change_grant",
        "oauth2_provider.delete_grant",
        "oauth2_provider.view_refreshtoken",
        "oauth2_provider.add_refreshtoken",
        "oauth2_provider.change_refreshtoken",
        "oauth2_provider.delete_refreshtoken",
        {%- endif %}
    ],
    "UNREGISTER_MODELS": [
        {%- if cookiecutter.use_drf == "y" %}
        "rest_framework.authtoken.models.TokenProxy",
        {%- endif %}
        # All-auth
        "allauth.account.models.EmailAddress",
        "allauth.socialaccount.models.SocialAccount",
        "allauth.socialaccount.models.SocialApp",
        "allauth.socialaccount.models.SocialToken",
        {%- if cookiecutter.use_celery == "y" %}
        # Celery
        "django_celery_beat.models.ClockedSchedule",
        # "django_celery_beat.models.CrontabSchedule",
        # "django_celery_beat.models.IntervalSchedule",
        # "django_celery_beat.models.PeriodicTask",
        "django_celery_beat.models.SolarSchedule",
        "django_celery_results.models.GroupResult",
        # "django_celery_results.models.TaskResult",
        {%- endif %}
        # "django.contrib.sites.models.Site",
        {%- if cookiecutter.use_oauth == "y" %}
        # oAuth2
        "oauth2_provider.models.IDToken",
        "oauth2_provider.models.Grant",
        {%- endif %}
    ],
}
{%- endif %}


{%- if cookiecutter.use_drf_api_logger == "y" %}
# drf-api-logger
# ------------------------------------------------------------------------------
# https://pypi.org/project/drf-api-logger/
DRF_API_LOGGER_DATABASE = True
DRF_API_LOGGER_SLOW_API_ABOVE = 200
DRF_API_LOGGER_TIMEDELTA = -240  # America/New_York
DRF_API_LOGGER_MAX_REQUEST_BODY_SIZE = 1024
DRF_API_LOGGER_MAX_RESPONSE_BODY_SIZE = 1024
DRF_API_LOGGER_PATH_TYPE = "FULL_PATH"
DRF_API_LOGGER_EXCLUDE_KEYS = ["AUTHORIZATION"]
{%- endif %}

# https://docs.djangoproject.com/en/4.2/howto/error-reporting/
IGNORABLE_404_URLS = [
    re.compile(r"'^/apple-touch-icon.*\.png$'"),
    re.compile(r"'^/favicon\.ico$'"),
    re.compile(r"'^/robots\.txt$'"),
]

PROJECT_TITLE = env("PROJECT_TITLE", default="{{ cookiecutter.project_name }}")
BASE_URL = env("BASE_URL", default="https://{{ cookiecutter.domain_name }}")

# Your stuff...
# ------------------------------------------------------------------------------
