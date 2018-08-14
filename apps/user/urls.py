# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/13 上午11:56' 

from django.conf.urls import url
from user import login_handler
from user import register_handler
from user import logout_handler
from user import views

urlpatterns = [
    url(r'^login/$', login_handler.LoginHandler, name='user_login'),
    url(r'^register/$', register_handler.RegisterHandler, name="user_register"),
    url(r'^logout/$', logout_handler.LogoutHandler),
    url(r'^active/$', register_handler.UserActivateHandler),
    url(r'^newtest/$', views.TestHandler),
]
