# Generated by Django 3.1.7 on 2021-04-24 06:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_auto_20210423_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='owner',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='main_page.account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 24, 13, 1, 21, 285562), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='account',
            name='telegram_id',
            field=models.IntegerField(blank=True, default=0, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='number',
            field=models.DecimalField(decimal_places=0, default='2404211301286562', max_digits=20, verbose_name='Номер сертификата'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 24, 13, 1, 21, 286562), null=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='url',
            field=models.URLField(default='https://mocerts.com/certificate/2404211301286562', max_length=255, verbose_name='Ссылка на серимфикат'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user1',
            field=models.CharField(default='Арина Моргунова', max_length=30, verbose_name='1 user'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user1_id',
            field=models.IntegerField(default=7413583),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user2',
            field=models.CharField(default='Лев Гаврилов', max_length=30, verbose_name='2 user'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user2_id',
            field=models.IntegerField(default=1648878),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user3',
            field=models.CharField(default='Виталий Титов', max_length=30, verbose_name='3 user'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user3_id',
            field=models.IntegerField(default=609391),
        ),
    ]
