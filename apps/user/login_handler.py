# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/13 下午3:21' 


from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect

from user import forms
from user import models

from django.views.decorators.csrf import csrf_exempt
from Wh1802Django import utils

#register: username: [zhangsan ]
#login:  username: [zhangsan]

@csrf_exempt
def LoginHandler(request):
	uloginform = forms.ArtsUserLoginForm()
	if request.method == "POST":
		uloginform = forms.ArtsUserLoginForm(data=request.POST)
		if not uloginform.is_valid(): #触发表单字段校验机制
			utils.flash(request, "error", f"用户登录失败！", level="error")
			return utils.render_context(request, "login_handler.html", uloginform)
		username = uloginform.cleaned_data.get('username', '')
		password = utils.create_pwd_md5(uloginform.cleaned_data.get('password', ''))
		user = models.ArtsUser.objects.filter(username=username, password=password, is_active=1).first()
		if user:
			request.session['muser'] = user
			return HttpResponseRedirect("/art/index")
		utils.flash(request, "error", f"用户{username}登录失败", level="error")

	return utils.render_context(request, "login_handler.html", uloginform)
