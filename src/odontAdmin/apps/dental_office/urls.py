# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^patients/', 'apps.dental_office.views.patients', name='patients'),
    url(r'^', 'apps.dental_office.views.home', name='home'),
]
