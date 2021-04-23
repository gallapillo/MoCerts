# Generated by Django 3.1.4 on 2020-12-18 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер сертификата')),
                ('url', models.URLField(max_length=255, verbose_name='Ссылка на серимфикат')),
                ('nominal', models.IntegerField(verbose_name='Номинал')),
                ('user1', models.CharField(max_length=30, verbose_name='1 user')),
                ('user2', models.CharField(max_length=30, verbose_name='2 user')),
                ('user3', models.CharField(max_length=30, verbose_name='3 user')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
