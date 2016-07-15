# -*- coding:utf-8 -*-
'''
Created on 2015-10-3

@author: Hyuang
'''

from django import forms
from homework.models import UserProfile

from captcha.fields import CaptchaField
from bootstrap_toolkit.widgets import BootstrapTextInput, BootstrapUneditableInput, BootstrapDateInput
class LoginForm(forms.Form):
    username = forms.CharField(
                               required = True,
                               label = u"用户名：",
                               error_messages = {'required':"请输入用户名"},
                               widget = forms.TextInput(attrs={'placeholder':u"用户名",}),
                               )
    password = forms.CharField(
                               required = True,
                               label = u"密码：",
                               error_messages = {'required':"请输入密码"},
                               widget = forms.PasswordInput(attrs={'placeholder':u"密码",}),                              
                               )
    captcha = CaptchaField(label = u"验证码：", required = True,  error_messages = {'required':"请输入验证码"})
    


TYPE_CHOICES = (('1', u'本科生'), ('2', u'研究生'), ('3', u'教师'), ('4', u'访客'),)

def validate_phone(value):
    if not value.isdigit():
        raise forms.ValidationError(u'%s不是电话号码' % value)
                
class RegisterForm(forms.Form):
    username = forms.CharField(
                               required = True,
                               label = u"*用户名：",
                               error_messages = {'required':"请输入用户名"},
                               widget = forms.TextInput(attrs={'placeholder':u"用户名",}),
                               )
    password1 = forms.CharField(label = u"*输入密码：", error_messages = {'required':"请输入密码"}, widget = forms.PasswordInput())  
    password2 = forms.CharField(label = u"*再次输入密码：", error_messages = {'required':"再次输入密码"}, widget = forms.PasswordInput())   
    email = forms.EmailField(label = u"*认证邮箱：", error_messages = {'required':"请输入邮箱"})
    phone = forms.CharField(label = u"电话号码：", required=False,validators=[validate_phone])
    type = forms.ChoiceField(label = u"*选择用户类型：", error_messages = {'required':"请选择用户类型"}, widget = forms.RadioSelect, choices = TYPE_CHOICES)
    stu_num = forms.CharField(label = u"学号：", error_messages = {'required':"学生请填写学号"})
    address = forms.CharField(label = u"工作单位：", error_messages = {'required':"其他用户请填写工作单位"})
    captcha = CaptchaField(label = u"验证码：", required = True,  error_messages = {'required':"请输入验证码"})
    class Meta:
        model = UserProfile
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        return cleaned_data
'''
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        address = cleaned_data.get('address')
        type = cleaned_data.get('type')
        stu_num = cleaned_data.get('stu_num')
'''
        
        