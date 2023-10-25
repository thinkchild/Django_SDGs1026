from django.contrib import admin
from .models import answer0,Person
from import_export.admin import ImportExportModelAdmin

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
  list_display = ('sID', 'stdName', 'stdPasswd', 'stdSex', 'stdGrade', 'stdClass', 'CP', 'CV')
admin.site.register(Person, PersonAdmin)