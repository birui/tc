import settings  
from django.conf.urls import patterns, include, url
from django.contrib import admin
from kz.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
]
