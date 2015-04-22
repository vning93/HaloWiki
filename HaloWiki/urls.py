from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HaloWiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^api/', include('api.urls', namespace="api")),
    url(r'^', include('api.urls', namespace="api")),
)