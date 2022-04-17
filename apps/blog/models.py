from django.db import models
import datetime
from mdeditor.fields import MDTextField
from user.models import User
# Create your models here.


# class User(models.Model):
#     username = models.CharField(max_length=20, unique=True, blank=False)
#     qq = models.CharField(max_length=11)
#     email = models.EmailField(blank=True, default='')
#     created_time = models.DateTimeField(auto_now_add=True)
#     updated_time = models.DateTimeField(auto_now=True)

# 后端
class Hd_study(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    read_count = models.IntegerField(default=0, verbose_name='浏览次数')
    praise_count = models.IntegerField(default=0, verbose_name='点赞次数')
    created_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '后端学习'
        verbose_name_plural = verbose_name


# 练字分享
class Practice(models.Model):
    text = models.TextField(verbose_name='练字分享文字内容')
    image = models.ImageField(upload_to='practice_images', verbose_name='练字图片')
    created_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = '练字分享'
        verbose_name_plural = '练字分享'


# 关于学习
class Study(models.Model):
    title = models.CharField(max_length=40, verbose_name='标题')
    introduce = models.CharField(max_length=70, verbose_name='引言', blank=True)
    content = MDTextField(verbose_name='内容')
    read_count = models.IntegerField(default=0, verbose_name='浏览次数')
    created_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '关于学习'
        verbose_name_plural = '关于学习'


class StudyComment(models.Model):
    user_image = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=30, verbose_name='姓名', unique=False)
    comment = models.CharField(max_length=200, verbose_name='评论')
    agree = models.IntegerField(default=0, verbose_name='点赞次数')
    created_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    article = models.ForeignKey(Study, on_delete=models.CASCADE, verbose_name='文章')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=8)

    class Meta:
        verbose_name = '关于学习评论'
        verbose_name_plural = '关于学习评论'
