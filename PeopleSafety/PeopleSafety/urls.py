from django.conf.urls import patterns, include, url
from PeopleSafety import views
from PeopleSafety.views import hello, current_datetime, search_form

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^hello/$', hello),
                       url(r'^time/$', current_datetime),
                       url(r'^search-form/$', search_form),
                       url(r'^search/$', views.search),
                       url(r'^unsafe-places/$', views.sampleMap)
)
