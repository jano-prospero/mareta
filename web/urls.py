"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

# Add the index request
def index(request):
    from django.shortcuts import render_to_response
    from django.template import RequestContext

    return render_to_response('base.html',
                                context_instance=RequestContext(request),
                            )

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='url_index'),

    #Apps urls
    url(r'^incident_handling$', include('web.apps.incident_handling.urls')),
    ]
