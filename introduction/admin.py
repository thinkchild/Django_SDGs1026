from django.contrib import admin
from .models import SDGs, Category

# Register your models here.
admin.site.register(SDGs)
admin.site.register(Category)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 