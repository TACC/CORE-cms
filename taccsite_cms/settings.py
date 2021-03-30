# taccsite_cms/settings.py

"""
Django settings for taccsite_cms project.

Generated by 'django-admin startproject' using Django 1.11.22.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import logging
import os
from glob import glob


def gettext(s): return s


# Import secret values dynamically without breaking portal.
def getsecrets():
    new_secrets = {};                                                                           # Var to hold secret values once imported succesfully.
    # Check for production secrets.
    try:
        print('Checking for secret production values')
        import taccsite_cms.secrets as secrets                                       # Prod/Staging/Local Dev values (used instead of the default values if present)
        new_secrets = secrets
        print('Production secrets found, using values')
    except ModuleNotFoundError as err:
        # Error handling
        print(err)
        print('No production secrets found')
        pass
        # Check for the default secret values.
        try:
            print('Checking for default secret values')
            import taccsite_cms.default_secrets as default_secrets            # Default demo values (works for basic local dev out of the box)
            new_secrets = default_secrets
            print('Default secrets found, using default values')
        except ModuleNotFoundError as err:
            # Error handling
            print(err)
            print('No default secrets found')
            print('Check that you have a secrets.py or default_secrets.py')
    finally:
        # Return the secret values if they are found.
        return new_secrets

# Assign secret settings values.
current_secrets = getsecrets()

# Boolean check to turn on/off console logging statements.
CONSOLE_LOG_ENABLED = current_secrets._CONSOLE_LOG_ENABLED

# Verifying console logging is on.
if CONSOLE_LOG_ENABLED:
    print("--> Variable CONSOLE_LOG_ENABLED: ", CONSOLE_LOG_ENABLED)

LDAP_ENABLED = current_secrets._LDAP_ENABLED

if CONSOLE_LOG_ENABLED:
    print("--> Variable LDAP_ENABLED: ", LDAP_ENABLED)

if LDAP_ENABLED:
    import ldap
    from django_auth_ldap.config \
        import LDAPSearch, GroupOfNamesType

DATA_DIR = os.path.dirname(os.path.dirname(__file__))

if CONSOLE_LOG_ENABLED:
    print("--> Variable DATA_DIR: ", DATA_DIR)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = current_secrets._SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = current_secrets._DEBUG

# Host Access.
ALLOWED_HOSTS = current_secrets._ALLOWED_HOSTS

# Custom Branding.
BRANDING = current_secrets._BRANDING
LOGO = current_secrets._LOGO
FAVICON = current_secrets._FAVICON

# Configure Portal.
PORTAL = current_secrets._PORTAL
PORTAL_AUTH_LINKS = current_secrets._PORTAL_AUTH_LINKS
PORTAL_UNAUTH_LINKS = current_secrets._PORTAL_UNAUTH_LINKS

# Optional features.
FEATURES = current_secrets._FEATURES

# Application definition
ROOT_URLCONF = 'taccsite_cms.urls'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

if CONSOLE_LOG_ENABLED:
    print("--> Variable STATIC_ROOT: ", STATIC_ROOT)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'taccsite_cms', 'static'),
    # os.path.join(BASE_DIR, 'taccsite_cms', 'en', 'static'),
) + tuple(glob(
    os.path.join(BASE_DIR, 'taccsite_custom', '*', 'static')
))

if CONSOLE_LOG_ENABLED:
    print("--> Variable STATICFILES_DIRS: ", STATICFILES_DIRS)

# User Uploaded Files Location.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

if CONSOLE_LOG_ENABLED:
    print("--> Variable MEDIA_ROOT: ", MEDIA_ROOT)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # FAQ: List custom directory first, so custom templates take precedence
        # SEE: https://docs.djangoproject.com/en/2.2/topics/templates/#configuration
        'DIRS': glob(
            os.path.join(BASE_DIR, 'taccsite_custom')
        ) + [
            os.path.join(BASE_DIR, 'taccsite_cms', 'templates')
        ],
        # 'APP_DIRS': True,
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
            'libraries': {
                # NOTE: These are an unnecessary alternative config, because taccsite_cms is in INSTALLED_APPS, but are comfortably explicit
                # SEE: https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/#code-layout
                'custom_portal_settings': 'taccsite_cms.templatetags.custom_portal_settings',
                'tacc_uri_shortcuts': 'taccsite_cms.templatetags.tacc_uri_shortcuts',
            },
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
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
    # Customize 'django.contrib.staticfiles'
    # SEE: https://stackoverflow.com/q/57921970/11817077
    # 'django.contrib.staticfiles',
    'taccsite_cms.django.contrib.staticfiles_custom',
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
    # 'djangocms_forms', # FP-416: Pending full support
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
    'haystack',
    'taccsite_cms',
]

# Convert list of paths to list of dotted module names
def get_subdirs_as_module_names(path):
    module_names = []
    for entry in os.scandir(path):
        if entry.is_dir():
            # FAQ: There are different root paths to tweak:
            #      - Containers use `/code/…`
            #      - Python Venvs use `/srv/taccsite/…`
            module_name = entry.path \
                .replace(os.path.sep + 'code' + os.path.sep, '') \
                .replace(os.path.sep + 'srv' + os.path.sep + 'taccsite' + os.path.sep, '') \
                .replace(os.path.sep, '.')
            module_names.append(module_name)
    return module_names

# Append CMS project paths as module names to INSTALLED_APPS
# FAQ: This automatically looks into `/taccsite_custom` and creates an "App" for each directory within
CUSTOM_CMS_DIR = os.path.join(BASE_DIR, 'taccsite_custom')
INSTALLED_APPS_APPEND = get_subdirs_as_module_names(CUSTOM_CMS_DIR)
INSTALLED_APPS = INSTALLED_APPS + INSTALLED_APPS_APPEND


if CONSOLE_LOG_ENABLED:
    print("--> Variable INSTALLED_APPS: ", INSTALLED_APPS)

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

if LDAP_ENABLED:
    AUTHENTICATION_BACKENDS.insert(0,
        "django_auth_ldap.backend.LDAPBackend"
    )

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

if getattr(current_secrets, '_CACHES', None):
    CACHES = secrets._CACHES                        # Are we actually using this setting?

DATABASES = current_secrets._DATABASES

MIGRATION_MODULES = { }

# SSL Setup.
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# DjangoCMS Setup.
SITE_ID = current_secrets._SITE_ID

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

CMS_TEMPLATES = current_secrets._CMS_TEMPLATES
CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)


# FEATURES.
if CONSOLE_LOG_ENABLED:
    print("--> Variable FEATURES: ")
    for feature in FEATURES:
        print(feature + ": ", FEATURES[feature])

if current_secrets._FEATURES['blog']:
    # Install required apps
    INSTALLED_APPS += [
        # Blog/News
        # 'filer',              # Already added
        # 'easy_thumbnails',    # Already added
        'aldryn_apphooks_config',
        'parler',
        'taggit',
        'taggit_autosuggest',
        'meta',                 # also supports `djangocms_page_meta`
        'sortedm2m',
        'djangocms_blog',

        # Metadata
        'djangocms_page_meta',
    ]

    # Metadata: Configure
    META_SITE_PROTOCOL = 'http'
    META_USE_SITES = True
    META_USE_OG_PROPERTIES = True
    META_USE_TWITTER_PROPERTIES = True
    META_USE_GOOGLEPLUS_PROPERTIES = True # django-meta 1.x+
    # META_USE_SCHEMAORG_PROPERTIES=True  # django-meta 2.x+

    # Blog/News: Set custom paths for templates
    BLOG_PLUGIN_TEMPLATE_FOLDERS = (
        ('plugins/default', 'Default template'),    # i.e. `templates/djangocms_blog/plugins/default/`
        ('plugins/default-clone', 'Clone of default template'),  # i.e. `templates/djangocms_blog/plugins/default-clone/`
    )

    # Blog/News: Change default values for the auto-setup of one `BlogConfig`
    # SEE: https://github.com/nephila/djangocms-blog/issues/629
    BLOG_AUTO_SETUP = True
    BLOG_AUTO_HOME_TITLE ='Home'
    BLOG_AUTO_BLOG_TITLE = 'News'
    BLOG_AUTO_APP_TITLE = 'News'


DJANGOCMS_PICTURE_NESTING = True
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES = True
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES_VIEWPORT_BREAKPOINTS = [
    576, 768, 992, 1200, 1400, 1680, 1920
]
DJANGOCMS_PICTURE_RATIO = 1.618

# FILE UPLOAD VALUES MUST BE SET!
# Set in correlation with the `client_max_body_size    20m;` value in /etc/nginx/proxy.conf.
# A problem comes from Django's usage of tempfile, which enforces new files to have permission
# 0600 and Django doesn't fix it unless FILE_UPLOAD_PERMISSIONS is defined.
# A tempfile is used when upload exceeds FILE_UPLOAD_MAX_MEMORY_SIZE.
FILE_UPLOAD_PERMISSIONS = 0o644
FILE_UPLOAD_MAX_MEMORY_SIZE = 20000000 # 20MB

# Custom picture templates - if required.
# DJANGOCMS_PICTURE_TEMPLATES = [
#     ('background', _('Background image')), # Need to design these first!
# ]

DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS = ['mp3', 'ogg', 'wav']
# Custom audio templates - if required.
# DJANGOCMS_AUDIO_TEMPLATES = [
#     ('feature', _('Featured Version')),
# ]

# Djangocms Forms Settings.
# SEE: https://github.com/mishbahr/djangocms-forms#configuration
DJANGOCMS_FORMS_PLUGIN_MODULE = ('Generic')
DJANGOCMS_FORMS_PLUGIN_NAME = ('Form')
# DJANGOCMS_FORMS_DEFAULT_TEMPLATE = 'djangocms_forms/form_template/default.html'
DJANGOCMS_FORMS_TEMPLATES = (
    ('djangocms_forms/form_template/default.html', ('Default')),
)
DJANGOCMS_FORMS_USE_HTML5_REQUIRED = False
# DJANGOCMS_FORMS_WIDGET_CSS_CLASSES = {'__all__': ('form-control', ) }
DJANGOCMS_FORMS_REDIRECT_DELAY = 10000  # 10 seconds

DJANGOCMS_FORMS_RECAPTCHA_PUBLIC_KEY = current_secrets._DJANGOCMS_FORMS_RECAPTCHA_PUBLIC_KEY
DJANGOCMS_FORMS_RECAPTCHA_SECRET_KEY = current_secrets._DJANGOCMS_FORMS_RECAPTCHA_SECRET_KEY

# Google Analytics.
GOOGLE_ANALYTICS_PROPERTY_ID  = current_secrets._GOOGLE_ANALYTICS_PROPERTY_ID
GOOGLE_ANALYTICS_PRELOAD = current_secrets._GOOGLE_ANALYTICS_PRELOAD

# SETTINGS VARIABLE EXPORTS.
# Use a custom namespace (using default settings.VARIABLE configuration)
SETTINGS_EXPORT_VARIABLE_NAME = 'settings'

# Elasticsearch Indexing
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': current_secrets._ES_HOSTS,
        'INDEX_NAME': current_secrets._ES_INDEX_PREFIX.format('cms'),
        'KWARGS': {'http_auth': current_secrets._ES_AUTH }
    }
}

ES_DOMAIN = current_secrets._ES_DOMAIN

# Exported settings.
SETTINGS_EXPORT = [
    'DEBUG',
    'BRANDING',
    'LOGO',
    'FAVICON',
    'PORTAL',
    'PORTAL_AUTH_LINKS',
    'PORTAL_UNAUTH_LINKS',
    'FEATURES',
    'GOOGLE_ANALYTICS_PROPERTY_ID',
    'GOOGLE_ANALYTICS_PRELOAD'
]

if CONSOLE_LOG_ENABLED:
    print("--> Variable SETTINGS_EXPORT: ")
    for setting in SETTINGS_EXPORT:
        print(setting)
