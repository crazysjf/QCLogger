from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^log/$', views.log, name='log'),
    url(r'^records/$', views.records, name='records'),
]