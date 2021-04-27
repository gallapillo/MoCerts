from django import forms
from django.forms import PasswordInput, TextInput, CharField, IntegerField
from main_page.names.names_generator import false_user
from .models import *


class certificateForm(forms.ModelForm):
    date_cert = datetime.today()
    # генерируем номер сертификата
    cert_num = date_cert.strftime("%d%m%y%H%M%f")
    usr1 = str(false_user())
    usr2 = false_user()
    usr3 = false_user()


    user1 = CharField(label='1.', widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 1','value': false_user(),
               'style': 'padding-top:3px; padding-bottom:6px; padding-left-20px; padding-right:52px; margin-top:220px; margin-right:300px; font-size: 16px; line-height: 20px;'}))
    user2 = CharField(label='2.', widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 2','value': false_user(),
               'style': 'padding-top:5px; padding-bottom:5px; padding-left-20px; padding-right:52px; margin-bottom:-8px;  font-size: 16px; margin-right:220px; line-height: 20px;'}))
    user3 = CharField(label='3', widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 3','value': false_user(),
               'style': 'padding-top:5px; padding-bottom:5px; padding-left-20px; padding-right:92px; font-size: 14px; margin-right:80px; line-height: 20px;'}))
    nominal = IntegerField(widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Цена',
               'style':'display: none; padding:10px 25px; font-size: 16px; line-height: 20px;','value': 1,'readonly':''}))
    number = IntegerField(widget=TextInput(
        attrs={'class': 'form-input',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;','value': cert_num,
               'readonly': ''}))
    class Meta:
        model = Certificate_1
        fields = ('user1','user2','user3','nominal','number',)


class certificateForm2(forms.ModelForm):
    user1 = CharField(widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 1',
               'style': 'padding:10px 25px; margin-top:218px; font-size: 16px; line-height: 20px;'}))
    user2 = CharField(widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 2',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))
    user3 = CharField(widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 3',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))
    nominal = IntegerField(widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Цена',
               'style':'display:none; padding:10px 25px; font-size: 16px; line-height: 20px;','value': 5,'readonly':''}))
    class Meta:
        model = Certificate_1
        fields = ('user1','user2','user3','nominal',)