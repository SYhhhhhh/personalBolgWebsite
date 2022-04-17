# Generated by Django 4.0.1 on 2022-02-04 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, upload_to='user_images', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ip',
            field=models.CharField(blank=True, max_length=20, verbose_name='ip'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=32, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.CharField(blank=True, max_length=11, verbose_name='qq'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, verbose_name='用户名'),
        ),
    ]
