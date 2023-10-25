from django.contrib import admin
from .models import Question, UserQuiz

admin.site.register(Question)
admin.site.register(UserQuiz)