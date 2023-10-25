from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class Question(models.Model):
    issue = models.CharField(max_length=255, null=True, blank=True)
    question = models.CharField(max_length=255)
    option_A = models.CharField(max_length=100)
    option_B = models.CharField(max_length=100)
    option_C = models.CharField(max_length=100)
    option_D = models.CharField(max_length=100)
    st_option = models.CharField(max_length=1, null=True, blank=True)
    correct_option = models.CharField(max_length=1)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


if not Permission.objects.filter(codename='can_view_score').exists():
    permission = Permission.objects.create(
        codename='can_view_score',     name='Can view score',
        content_type=ContentType.objects.get_for_model(Question),
    )


class UserQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=1, null=True, blank=True)