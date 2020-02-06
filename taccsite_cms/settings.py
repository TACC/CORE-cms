# taccsite_cms/settings.py

"""
Django settings for taccsite_cms project.

Generated by 'django-admin startproject' using Django 1.11.22.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Boolean check to turn on/off console logging statements.
CONSOLE_LOG_ENABLED = False
# Verifying console logging is on.
if CONSOLE_LOG_ENABLED:
    print("--> Variable CONSOLE_LOG_ENABLED: ", CONSOLE_LOG_ENABLED)

# Boolean check to see if ldap is being used by the site.
# Ensure the django-auth-ldap==2.0.0 package is uncommented
# in the requirements.txt file or installed if using ldap.
LDAP_ENABLED = True
if CONSOLE_LOG_ENABLED:
    print("--> Variable LDAP_ENABLED: ", LDAP_ENABLED)

import os  # isort:skip
import logging
import taccsite_cms.secrets as secrets

if LDAP_ENABLED:
    import ldap
    from django_auth_ldap.config \
        import LDAPSearch, GroupOfNamesType

def gettext(s): return s

DATA_DIR = os.path.dirname(os.path.dirname(__file__))
if CONSOLE_LOG_ENABLED:
    print("--> Variable DATA_DIR: ", DATA_DIR)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets._SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = secrets._DEBUG

ALLOWED_HOSTS = secrets._ALLOWED_HOSTS

# Custom Navigation Template.
NAVIGATION_TEMPLATE = secrets._NAVIGATION_TEMPLATE

# Application definition
ROOT_URLCONF = 'taccsite_cms.urls'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
if CONSOLE_LOG_ENABLED:
    print("--> Variable STATIC_ROOT: ", STATIC_ROOT)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'taccsite_cms', 'static'),
    # os.path.join(BASE_DIR, 'taccsite_cms', 'en', 'static'),
)
if CONSOLE_LOG_ENABLED:
    print("--> Variable STATICFILES_DIRS: ", STATICFILES_DIRS)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
if CONSOLE_LOG_ENABLED:
    print("--> Variable MEDIA_ROOT: ", MEDIA_ROOT)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'taccsite_cms', 'templates'), ],

        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
                'django_settings_export.settings_export'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]
if CONSOLE_LOG_ENABLED:
    print("--> Variable TEMPLATES: ", TEMPLATES)

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',  # Replaces mptt.
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    # 'djangocms_audio',
    'djangocms_column',
    'djangocms_file',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    'djangocms_icon',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'taccsite_cms'
]

# Comment the LDAPBackend to use local django auth
AUTHENTICATION_BACKENDS = [
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]

if LDAP_ENABLED:
    ''' LDAP Auth Settings '''
    AUTH_LDAP_SERVER_URI = "ldap://ldap.tacc.utexas.edu"
    AUTH_LDAP_CONNECTION_OPTIONS = {ldap.OPT_REFERRALS: 0}
    AUTH_LDAP_START_TLS = True
    AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = True

    AUTH_LDAP_BIND_DN = ""
    AUTH_LDAP_BIND_PASSWORD = ""
    AUTH_LDAP_USER_SEARCH = LDAPSearch(
        "ou=People,dc=tacc,dc=utexas,dc=edu", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
    )

    AUTH_LDAP_AUTHORIZE_ALL_USERS = True

    AUTH_LDAP_USER_ATTR_MAP = {
        "first_name": "givenName",
        "last_name": "sn",
        "email": "mail",
    }

    '''
     # More customizations

     AUTH_LDAP_REQUIRE_GROUP = "cn=TACC-ACI-WMA,ou=Groups,dc=tacc,dc=utexas,dc=edu"
     AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
         "ou=Groups,dc=tacc,dc=utexas,dc=edu",
         ldap.SCOPE_SUBTREE,
         "(objectClass=groupOfUniqueNames)",
     )
     AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
    '''
    ''' End LDAP Auth Settings '''

if getattr(secrets, '_CACHES', None):
    CACHES = secrets._CACHES

DATABASES = {
    'default': {
        'ENGINE': secrets._DATABASE_ENGINE,
        'NAME': secrets._DATABASE_NAME,
        'USER': secrets._DATABASE_USERNAME,
        'PASSWORD': secrets._DATABASE_PASSWORD,
        'HOST': secrets._DATABASE_HOST,
        'PORT': secrets._DATABASE_PORT,
    }
}

MIGRATION_MODULES = {

}

# SSL Setup.
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# DjangoCMS Setup.
SITE_ID = secrets._SITE_ID

LANGUAGES = (
    # Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    # Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = secrets._CMS_TEMPLATES
CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

DJANGOCMS_PICTURE_NESTING = True
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES = True
DJANGOCMS_PICTURE_RATIO = 1.618
# Custom picture templates - if required.
# DJANGOCMS_PICTURE_TEMPLATES = [
#     ('background', _('Background image')), # Need to design these first!
# ]

DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS = ['mp3', 'ogg', 'wav']
# Custom audio templates - if required.
# DJANGOCMS_AUDIO_TEMPLATES = [
#     ('feature', _('Featured Version')),
# ]

# Google Analytics.
GOOGLE_ANALYTICS_PROPERTY_ID = secrets._GOOGLE_ANALYTICS_PROPERTY_ID
GOOGLE_ANALYTICS_PRELOAD = secrets._GOOGLE_ANALYTICS_PRELOAD

# SETTINGS VARIABLE EXPORTS.
# Use custom namespace instead of default settings.VARIABLE.
SETTINGS_EXPORT_VARIABLE_NAME = 'portal_settings'
# Exported settings.
SETTINGS_EXPORT = [
    'DEBUG',
    'NAVIGATION_TEMPLATE',
    'GOOGLE_ANALYTICS_PROPERTY_ID',
    'GOOGLE_ANALYTICS_PRELOAD'
]

if CONSOLE_LOG_ENABLED:
    print(SETTINGS_EXPORT[1])
    print(SETTINGS_EXPORT[2])
    print(SETTINGS_EXPORT[3])
