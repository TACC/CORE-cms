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
]

if settings.PORTAL:
    from django.views.generic.base import TemplateView
    urlpatterns += [
        # FAQ: Allows direct access to isolated CMS menu markup for the Portal and User Guide to render
        url(r'^cms/nav/pages/markup/$', TemplateView.as_view(template_name='cms_menu.html'), name='menu_pages_markup'),
    ]

urlpatterns += [
    url(r'^admin/', admin.site.urls),  # NOQA
    url(r'^', include('cms.urls')),
]

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ]

    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
