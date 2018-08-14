# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/14 上午11:41' 

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect

from user import forms
from user import models

from django.views.decorators.csrf import csrf_exempt
from Wh1802Django import utils

def LogoutHandler(request):
	'''
	用户注销
	:param request:
	:return:
	'''
	del request.session['muser']
	return HttpResponseRedirect('/user/login')
