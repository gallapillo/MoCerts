from django.db import models

from django.db import models
from django import forms
from django.utils import timezone
from django.conf import settings
from datetime import datetime

from .names.names_generator import false_user
import random
from django.contrib.auth.models import User
from django.conf import settings


class Account(models.Model):
    '''Модель для пользователя'''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tlg_id = models.IntegerField(
        unique=True, name='telegram_id', null=True, blank=True, default=0)
    username = models.CharField(
        max_length=50, verbose_name='username', blank=True)
    full_name = models.CharField(
        max_length=50, verbose_name='full name', default=None)
    phone = models.CharField(max_length=50, verbose_name='phone', blank=True)
    email = models.EmailField(max_length=50, verbose_name='email_field')
    balance = models.DecimalField(
        max_digits=6, decimal_places=1, verbose_name='balance', default=0)
    language_code = models.CharField(
        max_length=10, verbose_name='language code', default='en')
    date_joined = models.DateTimeField(
        verbose_name='date joined', default=datetime.now())
    certificate_quantity = models.IntegerField(
        verbose_name='certificate quantity', default=0)


    def publish(self):
        self.date_joined = datetime.now()
        self.save()

    def __str__(self):
        return f'Пользователи {self.username}: date({self.date_joined})'


class Certificate(models.Model):
    date_cert = datetime.today()
    # генерируем номер сертификата
    cert_num = date_cert.strftime("%d%m%y%H%M%f")
    number = models.DecimalField(verbose_name='Номер сертификата', max_digits=20, decimal_places=0,
                                 default=cert_num)
    url = models.URLField(max_length=255, verbose_name='Ссылка на серимфикат',
                          default=f'https://mocerts.com/certificate/{cert_num}')
    nominal = models.IntegerField(verbose_name='Номинал', default=1)

    user1 = models.CharField(
        max_length=30, verbose_name='1 user', default=false_user())
    user1_id = models.IntegerField(
        name='user1_id', default=random.randint(1000, 10000000))

    user2 = models.CharField(
        max_length=30, verbose_name='2 user', default=false_user())
    user2_id = models.IntegerField(
        name='user2_id', default=random.randint(1000, 10000000))

    user3 = models.CharField(
        max_length=30, verbose_name='3 user', default=false_user())
    user3_id = models.IntegerField(
        name='user3_id', default=random.randint(1000, 10000000))

    published_date = models.DateTimeField(
        blank=True, null=True, default=date_cert)

    owner = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Владелец Сертификата')


    def new_cert(self):
        date_cert = datetime.today()
        self.cert_num = date_cert.strftime("%d%m%y%H%M%f")
        self.url = f'https://mcert.me/certificate/{self.cert_num}'
        self.nominal = 1
        self.user1 = false_user()
        self.user2 = false_user()
        self.user3 = false_user()
        self.published_date = datetime.today()
        new_cert = dict(cert_num=self.cert_num,
                        url=self.url,
                        nominal=self.nominal,
                        user1=self.user1,
                        user2=self.user2,
                        user3=self.user3,
                        published_date=self.published_date)
        return new_cert

    def publish(self):
        self.published_date = datetime.now()
        self.save()

    def __str__(self):
        return f'Сертификат {self.number}'








cert = Certificate()
new_cert = cert.new_cert()
print(new_cert)
