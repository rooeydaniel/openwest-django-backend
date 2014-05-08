"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project

https://docs.djangoproject.com/en/1.6/topics/http/urls/
"""
from django.conf.urls import patterns, url, include

from django.contrib import admin
# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#discovery-of-admin-files
admin.autodiscover()

# The 'r' in front of each regular expression string is optional but recommended.
# It tells Python that a string is "raw" - that nothing in the string should be escaped.
urlpatterns = patterns('',
    # https://docs.djangoproject.com/en/1.6/ref/contrib/admin/admindocs/
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # https://docs.djangoproject.com/en/1.6/ref/contrib/admin/
    url(r'^admin/', include(admin.site.urls)),

    # https://docs.djangoproject.com/en/1.6/ref/urls/#include
    url(r'^', include('task.urls')),
)