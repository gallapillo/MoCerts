from django import forms
from django.forms import PasswordInput, TextInput, CharField, IntegerField

from .models import *


class certificateForm(forms.ModelForm):
    user1 = CharField(widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 1',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))
    user2 = CharField(label='Имя 2', widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 2',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))
    user3 = CharField(label='Имя 3', widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 3',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))
    nominal = IntegerField(label='Цена', widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Цена',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;','value': 1,'readonly':''}))
    class Meta:
        model = Certificate
        fields = ('user1','user2','user3','nominal',)


class certificateForm2(forms.ModelForm):
    user1 = CharField(widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 1',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))
    user2 = CharField(label='Имя 2', widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 2',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))
    user3 = CharField(label='Имя 3', widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 3',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;'}))
    nominal = IntegerField(label='Цена', widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Цена',
               'style': 'padding:10px 25px; font-size: 16px; line-height: 20px;','value': 5,'readonly':''}))
    class Meta:
        model = Certificate
        fields = ('user1','user2','user3','nominal',)