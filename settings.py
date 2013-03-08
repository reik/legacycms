import sys, os

APP_BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if APP_BASEDIR not in sys.path:
    sys.path.insert(0, APP_BASEDIR)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('reik', 'kurarei@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'legacycms.db')

DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': DATABASE_NAME,
}}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = int(os.environ.get('SITE_ID', 1))

USE_I18N = True

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static/')
STATIC_URL = '/static/'

SECRET_KEY = '_wn95s-apfd-442cby5m^_^ak6+5(fyn3lvnvtn7!si&o)1x^w'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'feincms.context_processors.add_page_if_missing',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)
ROOT_URLCONF = 'legacycms.urls'

TEMPLATE_DIRS = (os.path.join(APP_BASEDIR, "templates"),)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'legacycms.email_usernames.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PROFILE_MODULE = 'profiles.UserProfile'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    'feincms',
    'feincms.module.blog',
    'feincms.module.page',
    'feincms.module.medialibrary',
    'mptt',
    'south',
    'legacycms',
    'profiles',
    'gallery',
    'debug_toolbar',
)

LANGUAGES = (
    ('en', 'English'),
    ('de', 'German'),
)

FEINCMS_TREE_EDITOR_INCLUDE_ANCESTORS = True

ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_URL          = 'accounts/login/'
LOGIN_REDIRECT_URL = '/'

AUTH_PROFILE_MODULE = "legacycms.UserProfile"
