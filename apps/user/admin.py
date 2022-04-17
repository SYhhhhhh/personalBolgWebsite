from django.contrib import admin
from user.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'qq', 'created_time', 'ip']
    readonly_fields = ['id', 'username', 'password', 'qq', 'created_time', 'ip']
