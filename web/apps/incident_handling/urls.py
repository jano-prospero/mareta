from django.conf.urls import patterns, url

urlpatterns = patterns('web.apps.incident_handling.views',
    url(r'^$', 'view_incident_handling', name='url_incident_handling'),
    )
