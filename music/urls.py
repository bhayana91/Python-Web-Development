# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:20:13 2017

@author: dell
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    #/music/    
    url(r'^$', views.index, name='index'),
    #/music/71
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
