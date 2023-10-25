from django.contrib import admin
from .models import UserProfile
from django.contrib import admin
# admin.py

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'stdsex', 'cp', 'cv')  # 用于显示在用户列表的字段
    search_fields = ('user__username', 'stdsex')  # 允许搜索的字段

admin.site.register(UserProfile, UserProfileAdmin)

