import settings  
from django.conf.urls import patterns, include, url
from django.contrib import admin
from kz.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^$', home),
    # url(r'^(?P<my_args>\d+)/$', detail),
    url(r'^base/$', base),
    url(r'^law/$', law),
    url(r'^(?P<id>\d+)/$', detail),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]
