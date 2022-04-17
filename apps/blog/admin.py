from django.contrib import admin
from blog.models import Hd_study, Practice, Study, StudyComment
from django.utils.html import format_html
# Register your models here.


# 后端学习
@admin.register(Hd_study)
class Blog(admin.ModelAdmin):
    list_display = ['title', 'content', 'read_count', 'praise_count', 'created_time']
    readonly_fields = ['created_time', 'read_count', 'praise_count']
    search_fields = ['title']


# 练字分享
@admin.register(Practice)
class Practice(admin.ModelAdmin):
    list_display = ['id', 'text', 'created_time', 'image']
    readonly_fields = ['id', 'created_time']
    search_fields = ['id']


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'introduce', 'content', 'created_time']
    readonly_fields = ['id', 'created_time']
    search_fields = ['title']


@admin.register(StudyComment)
class StudyCommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'comment', 'agree', 'created_time', 'article']
    readonly_fields = ['created_time']
    search_fields = ['username', 'article_id']
