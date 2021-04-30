from django.db import models

from django.db import models
from django import forms
from django.utils import timezone
from django.conf import settings
from datetime import datetime

from blog.models import Certificate_1
from .names.names_generator import false_user
import random
from django.contrib.auth.models import User
from django.conf import settings


class Account(models.Model):
    '''Модель для пользователя'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tlg_id = models.IntegerField(
        unique=True, name='telegram_id', null=True, blank=True, default=0)
    username = models.CharField(
        max_length=50, verbose_name='username', blank=True)
    full_name = models.CharField(
        max_length=50, verbose_name='full name', default=None)
    phone = models.CharField(max_length=50, verbose_name='phone', blank=True)
    email = models.EmailField(max_length=50, verbose_name='email_field')
    balance = models.IntegerField(
         verbose_name='balance', default=0)
    language_code = models.CharField(
        max_length=10, verbose_name='language code', default='en')
    date_joined = models.DateTimeField(
        verbose_name='date joined', default=datetime.now())
    certificate_quantity = models.IntegerField(
        verbose_name='certificate quantity', default=0)
    cert_1 = models.ManyToManyField(Certificate_1, null=True,blank=True)

    def publish(self):
        self.date_joined = datetime.now()
        self.save()

    def __str__(self):
        return f'Пользователи {self.username}: date({self.date_joined})'











cert = Certificate_1()
new_cert = cert.new_cert()
print(new_cert)
