import os

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps import Sitemap, FlatPageSitemap

sitemaps = {
  'site': Sitemap,
}

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls) ),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), 'media/')}),
    url(r'^accounts/', include('legacycms.email_usernames.urls')),
    url(r'^profiles/', include('legacycms.profiles.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps }),
    url(r'', include('feincms.contrib.preview.urls')),
    url(r'', include('feincms.urls')),
) + staticfiles_urlpatterns()
