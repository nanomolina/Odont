# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^', 'apps.core.views.home', name='home'),
]
