from django.db import models
import datetime


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    qq = models.CharField(max_length=11, blank=True, verbose_name='qq')
    ip = models.CharField(max_length=20, blank=True, verbose_name='ip')
    image = models.FileField(upload_to='user_images', blank=True, verbose_name='头像')
    created_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.username
