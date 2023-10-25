from django.db import models
from django import forms
from django.utils import timezone

# Create your models here.
# quiz_app/models.py
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stdsex = models.CharField(max_length=10)
    cp = models.IntegerField(default=0)
    cv = models.IntegerField(default=0)
    has_answered= models.BooleanField(default=False)

class UserProfileAdminForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'  # 或选择要显示的字段
