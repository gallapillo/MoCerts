from django.db import models
from django.utils import timezone
from django.conf import settings
from datetime import datetime

# Create your models here.

#1 Certificate id
#----------------------
#2 Number
#3 Nominal
#-------------------------
#4 FirstUser
#5 SecondUser
#6 TheardUser


class User(models.Model):
    tlg_id = models.IntegerField(unique=True, name='telegram_id')
    username = models.CharField(max_length=50, verbose_name='username')
    full_name = models.CharField(max_length=50, verbose_name='full name', default=None)
    phone = models.CharField(max_length=50, verbose_name='phone')
    emale = models.EmailField(max_length=50, verbose_name='email_field', blank=True)
    balance = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='balance', blank=False)
    language_code = models.CharField(max_length=10, verbose_name='language code')
    date_joined = models.DateTimeField(verbose_name='date joined')
    certificate_quantity = models.IntegerField(verbose_name='certificate quantity', primary_key=0)

    def publish(self):
        self.date_joined = datetime.now()
        self.save()

    def __str__(self):
        return f'Пользователи {self.username}'

class Certificate(models.Model):
    number = models.IntegerField(verbose_name='Номер сертификата')
    url = models.URLField(max_length=255, verbose_name='Ссылка на серимфикат')
    nominal = models.IntegerField(verbose_name='Номинал')
    user1 = models.CharField(max_length=30, verbose_name='1 user')
    user2 = models.CharField(max_length=30, verbose_name='2 user')
    user3 = models.CharField(max_length=30, verbose_name='3 user')
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = datetime.now()
        self.save()


    def __str__(self):
        return f'Сертификат {self.number}'