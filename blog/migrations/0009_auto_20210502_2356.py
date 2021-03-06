# Generated by Django 3.1.7 on 2021-05-02 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210429_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate_1',
            name='number',
            field=models.DecimalField(decimal_places=0, default='0205212356020667', max_digits=20, verbose_name='Номер сертификата'),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 2, 23, 56, 25, 20667), null=True),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='status',
            field=models.CharField(blank=True, choices=[('val1', 'Отправлен'), ('val2', 'Получен'), ('val3', 'Оплачен'), ('val4', 'Неотправлен')], default='val3', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='url',
            field=models.URLField(default='https://mocerts.com/certificate/0205212356020667', max_length=255, verbose_name='Ссылка на серимфикат'),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user1',
            field=models.CharField(default='Николай Малышев', max_length=30, verbose_name='1 user'),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user1_id',
            field=models.IntegerField(default=3099556),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user2',
            field=models.CharField(default='Тимур Колосов', max_length=30, verbose_name='2 user'),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user2_id',
            field=models.IntegerField(default=5905142),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user3',
            field=models.CharField(default='Руслан Любимов', max_length=30, verbose_name='3 user'),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user3_id',
            field=models.IntegerField(default=7322929),
        ),
    ]
