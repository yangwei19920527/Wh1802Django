# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/13 下午3:46' 
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from Wh1802Django.utils import check_user_login


@check_user_login
def IndexHandler(request):
	print(request.COOKIES)
	request.session['name'] = 'xidada'
	print(request.session)
	return render(request, "home/index_handler.html")
