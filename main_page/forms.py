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
               'style': 'background-color: transparent;  border: none; color: #fff; padding-top:3px; padding-bottom:6px; padding-left-20px; padding-right:52px; margin-top:220px; margin-right:300px; font-size: 16px; line-height: 20px;'}))
    user2 = CharField(label='2.', widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 2','value': false_user(),
               'style': 'background-color: transparent; border: none; color: #fff; padding-top:5px; padding-bottom:5px; padding-left-20px; padding-right:52px; margin-bottom:-8px;  font-size: 16px; margin-right:220px; line-height: 20px;'}))
    user3 = CharField(label='3', widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Имя 3','value': false_user(),
               'style': 'background-color: transparent;  border: none; color: #fff; padding-top:5px; padding-bottom:5px; padding-left-20px; padding-right:92px; font-size: 14px; margin-right:80px; line-height: 20px;'}))
    nominal = IntegerField(widget=TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Цена',
               'style':'background-color: transparent; display: none; padding:10px 25px; font-size: 16px; line-height: 20px;','value': 1,'readonly':''}))
    number = IntegerField(widget=TextInput(
        attrs={'class': 'form-input',
               'style': 'background-color: transparent;  border: none; color: #fff; padding:10px 25px; font-size: 16px; line-height: 20px;','value': cert_num,
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


class RegistrationForm(forms.ModelForm):

    username = forms.CharField(required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите Пароль'
        self.fields['phone'].label = 'Телефон'
        self.fields['email'].label = 'Почта'
        self.fields['full_name'].label = 'Полное имя'

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f"Данный почтовый адрес зареган")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f"Данный {username} Акк зареган")
        return username


    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError(f"Пароли не совподают")

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username','password','confirm_password','full_name','email','phone']



class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином {username} не найден в системе. ')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']