# Generated by Django 3.1.7 on 2021-04-23 04:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_auto_20210423_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 23, 11, 10, 5, 411159), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='account',
            name='telegram_id',
            field=models.IntegerField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='number',
            field=models.DecimalField(decimal_places=0, default='2304211110413160', max_digits=20, verbose_name='Номер сертификата'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 23, 11, 10, 5, 413160), null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='url',
            field=models.URLField(default='https://mocerts.com/certificate/2304211110413160', max_length=255, verbose_name='Ссылка на серимфикат'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user1',
            field=models.CharField(default='Елена Алешина', max_length=30, verbose_name='1 user'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user1_id',
            field=models.IntegerField(default=8681959),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user2',
            field=models.CharField(default='Николай Кольцов', max_length=30, verbose_name='2 user'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user2_id',
            field=models.IntegerField(default=5526503),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user3',
            field=models.CharField(default='Василий Березин', max_length=30, verbose_name='3 user'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user3_id',
            field=models.IntegerField(default=1947869),
        ),
    ]
