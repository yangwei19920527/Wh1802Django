# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/13 下午5:35' 

from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect

from user import forms
from user import models

from django.views.decorators.csrf import csrf_exempt
from Wh1802Django import utils
from Wh1802Django import settings

@csrf_exempt
def RegisterHandler(request):
    '''
	用户注册功能
	'''
    userform = forms.ArtsUserRegForm()
    if request.method == "POST":
        userform = forms.ArtsUserRegForm(data=request.POST)
        if not userform.is_valid():  #form表单校验失败
            #TODO:实现闪存消息，刷错误信息
            utils.flash(request, "error", f"用户注册信息失败", level="error")
            context = dict(
				form = userform
			)
            return render(request, "register_handler.html", context=context)
        #成功，保存db数据库
        username = userform.cleaned_data.get('username', '')
        password = utils.create_pwd_md5(userform.cleaned_data.get('password', ''))
        email = userform.cleaned_data.get('email', '')
        art_user = models.ArtsUser(username=username, password=password, email=email)
        art_user.save()
        #return  HttpResponseRedirect("/user/login")
        #utils.flash(request, "success", "用户注册成功！", level="success")



        #TODO: 发送激活邮件
        import uuid
        token = str(uuid.uuid4())
        activate_url = "http://%s:%s/user/active/?token=%s" % (settings.DJANGO_SERVICE[0],
                                          settings.DJANGO_SERVICE[1], token)

        #同步方式发送邮件
        utils.send_mail_to(username, activate_url, email, "注册邮箱激活页面")

        art_user.token = token
        art_user.save()

        utils.flash(request, "success", f"用户注册邮件发送成功，请查收{email}！", level="success")
    context = dict(
		form = userform
	)

    return render(request, "register_handler.html", context=context)



def UserActivateHandler(request):
    token = request.GET.get("token", "")
    user = models.ArtsUser.objects.get(token = token)
    if user:
        user.is_active = 1
        user.save()
        return HttpResponse(f"恭喜，用户{user.username} 激活成功！")
    return HttpResponse(f"激活用户信息失败，请重新注册。")


