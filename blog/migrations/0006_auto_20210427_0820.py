# Generated by Django 3.1.7 on 2021-04-27 01:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210427_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate_1',
            name='number',
            field=models.DecimalField(decimal_places=0, default='2704210820626281', max_digits=20, verbose_name='Номер сертификата'),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 27, 8, 20, 56, 626281), null=True),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='url',
            field=models.URLField(default='https://mocerts.com/certificate/2704210820626281', max_length=255, verbose_name='Ссылка на серимфикат'),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user1',
            field=models.CharField(default='Руслан Игнатов', max_length=30, verbose_name='1 user'),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user1_id',
            field=models.IntegerField(default=898434),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user2',
            field=models.CharField(default='Михаил Плотников', max_length=30, verbose_name='2 user'),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user2_id',
            field=models.IntegerField(default=8771223),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user3',
            field=models.CharField(default='Марк Павловский', max_length=30, verbose_name='3 user'),
        ),
        migrations.AlterField(
            model_name='certificate_1',
            name='user3_id',
            field=models.IntegerField(default=6308949),
        ),
    ]
