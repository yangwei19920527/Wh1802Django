# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/13 下午5:31' 

from django import forms
from django.forms import widgets
from Wh1802Django.settings import SEX_CHOICES, DB_FIELD_VALID_CHOICES, PAY_CHOICES
from user import models
from django.core.exceptions import  ValidationError

'''
会员注册表单
'''
class ArtsUserRegForm(forms.Form):
   username = forms.CharField(
      label = "用户名",
      required = True,
      min_length = 3,
      max_length = 50,
      widget = widgets.TextInput(
         attrs={
            "class":"form-control",
            "placeholder":"请输入用户名, 长度为3~50",
         }),
      error_messages = {
         "required":"对不起，用户名不能为空！",
         "min_length":"不行，长度小于3",
         "max_length":"sorry, 长度太长，大于50",
      }
   )
   password = forms.CharField(
      label="密码",
      required=True,
      min_length=6,
      max_length=20,
      widget=widgets.PasswordInput(
         attrs={
            "class": "form-control",
            "placeholder": "请输入密码, 长度为6~20",
         }),
      error_messages={
         "required": "对不起，密码不能为空！",
         "min_length": "不行，长度小于6",
         "max_length": "sorry, 长度太长，大于20",
      }
   )
   email = forms.EmailField(
      label="邮箱",
      required=True,
      widget=widgets.TextInput(
         attrs={
            "class": "form-control",
            "placeholder": "请输入邮箱",
         }),
      error_messages={
         "required": "对不起，邮箱不能为空！",
      }
   )

   def clean_username(self):
      #对username字段进行扩展校验
      username = self.cleaned_data.get("username", "")
      users = models.ArtsUser.objects.filter(username=username).count()
      if users:
         raise  ValidationError("用户已经存在！")
      return username

   def clean_email(self):
      #对email字段进行校验
      email = self.cleaned_data.get("email", "")
      users = models.ArtsUser.objects.filter(email=email).count()
      if users:
         raise  ValidationError("邮箱已经存在！")
      return email


'''
用户登录表单
'''
class ArtsUserLoginForm(forms.Form):
   username = forms.CharField(
      label="用户名",
      required=True,
      min_length=3,
      max_length=50,
      widget=widgets.TextInput(
         attrs={
            "class": "form-control",
            "placeholder": "请输入用户名, 长度为3~50",
         }),
      error_messages={
         "required": "对不起，用户名不能为空！",
         "min_length": "不行，长度小于3",
         "max_length": "sorry, 长度太长，大于50",
      }
   )
   password = forms.CharField(
      label="密码",
      required=True,
      min_length=6,
      max_length=20,
      widget=widgets.PasswordInput(
         attrs={
            "class": "form-control",
            "placeholder": "请输入密码, 长度为6~20",
         }),
      error_messages={
         "required": "对不起，密码不能为空！",
         "min_length": "不行，长度小于6",
         "max_length": "sorry, 长度太长，大于20",
      }
   )

