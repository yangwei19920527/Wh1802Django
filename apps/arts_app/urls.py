# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/13 上午11:56'

from django.conf.urls import url
from arts_app import index_handler

urlpatterns = [
    url(r'^index/', index_handler.IndexHandler),
]
