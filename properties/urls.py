__author__ = 'benfishman'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<property_id>[0-9]+)/detail/$', views.propertyDetail, name='propertyDetail'),
]