# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/14 上午10:01' 

from django.contrib import messages

from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from functools import wraps

from django.core.mail import send_mail
from django.template import loader
from Wh1802Django import settings

def create_pwd_md5(str_pwd, type='md5'):
   import hashlib
   h1 = hashlib.md5() if  type == "md5" else hashlib.sha1()
   h1.update(str_pwd.encode(encoding="utf-8"))
   return h1.hexdigest()


def render_context(request, template_name, form, *args, **kwargs):
    context = dict(
		form = form,
	)
    return render(request, template_name, context=context)


'''
django后台向前端发送一个闪现消息
利用django自带的message系统发送消息
'''
def flash(request, title, text, level='info'):
    LEVEL_MAP = {
		'info':messages.INFO,
		'debug':messages.DEBUG,
		'success':messages.SUCCESS,
		'warning':messages.WARNING,
		'error':messages.ERROR,
	}
    level = LEVEL_MAP[level]
    messages.add_message(request, level, text, title)
    return HttpResponse(text)


'''
装饰器，权限校验，用户登录才能进行功能放开
'''
def check_user_login(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        request = args[0]
        if  request.session.get("muser", None) == None:
            return HttpResponseRedirect("/user/login")
        return func(*args, **kwargs)
    return __wrapper




def send_mail_to(username,  active_url, receive_mail, title="xxx"):

    subject = "欢迎使用书城电商平台-邮件激活"

    temp = loader.get_template('user_active.html')

    data = {
        "username": username,
        "active_url": active_url,
		"title":title,
    }

    html_message = temp.render(context=data)

    send_mail(subject, title, from_email=settings.EMAIL_HOST_USER, recipient_list=[receive_mail],
              html_message=html_message)

