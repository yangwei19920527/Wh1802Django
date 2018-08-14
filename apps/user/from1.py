#coding:utf-8
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from user.models import ArtsUser

__author__ = 'aha'
__data__ = '2018/8/14/20:21'


class ArtsUserRegForm(forms.Form):
    username = forms.CharField(
        label='',
        required=True,
        min_length=8,
        max_length=30,
        widget=widgets.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"請輸入用戶名,長度為8~30",
            }
        ),
        error_messages={
            "required":"不能為空",
            "min_length":"長度不得小於8",
            "max_length":"長度不得大於30",
        }
    )

    password = forms.CharField(
        label='密碼',
        required=True,
        min_length=8,
        max_length=30,
        widget=widgets.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"輸入密碼,長度為8~30",
            }
        ),
        error_messages={
            "required":"密碼不得為空!",
            "min_length":"長度不得小於8",
            "max_length":"長度不得大於30",
        }
    )
    email = forms.CharField(
        label='密碼',
        required=True,
        widget = widgets.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"請輸入郵箱",
            }
        ),
        error_messages={
            'required':"郵箱不得為空"
        }
    )

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        users = ArtsUser.objects.filter(username=username)
        if users:
            raise ValidationError('用戶已經存在!')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        users = ArtsUser.objects.filter(email=email)
        if users:
            raise ValidationError('郵箱已經存在!')

