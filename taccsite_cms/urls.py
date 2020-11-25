# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),

    url(r'^admin/', admin.site.urls),  # NOQA
]

if settings.PORTAL:
    from django.views.generic.base import TemplateView
    urlpatterns += [
        # FAQ: Allows direct access to isolated CMS menu markup for the Portal and User Guide to render
        url(r'^cms/nav/pages/markup/$', TemplateView.as_view(template_name='nav_cms.raw.html'), name='menu_pages_markup'),

if settings.FEATURES['blog']:
    urlpatterns += [
        # Support `taggit_autosuggest` (from `djangocms-blog`)
        url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    ]

urlpatterns += [
    url(r'^', include('cms.urls')),
]

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ]

    urlpatterns += staticfiles_urlpatterns()

    # RFE: Would preventing cache be a good addition?
    # SEE: https://stackoverflow.com/a/59340216/11817077
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
