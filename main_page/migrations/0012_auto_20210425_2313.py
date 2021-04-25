# Generated by Django 3.1.7 on 2021-04-25 16:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_page', '0011_auto_20210425_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 25, 23, 13, 54, 721321), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='number',
            field=models.DecimalField(decimal_places=0, default='2504212313722322', max_digits=20, verbose_name='Номер сертификата'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец Сертификата'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 25, 23, 13, 54, 722322), null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='url',
            field=models.URLField(default='https://mocerts.com/certificate/2504212313722322', max_length=255, verbose_name='Ссылка на серимфикат'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user1',
            field=models.CharField(default='Станислав Дубинин', max_length=30, verbose_name='1 user'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user1_id',
            field=models.IntegerField(default=9486561),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user2',
            field=models.CharField(default='Павел Софронов', max_length=30, verbose_name='2 user'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user2_id',
            field=models.IntegerField(default=1218449),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user3',
            field=models.CharField(default='Арина Селиванова', max_length=30, verbose_name='3 user'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user3_id',
            field=models.IntegerField(default=2319716),
        ),
    ]
