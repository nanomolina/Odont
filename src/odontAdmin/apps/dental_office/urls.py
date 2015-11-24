# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^', 'apps.dental_office.views.ejemplo', name='ejemplo'),
]
