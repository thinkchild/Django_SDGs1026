from django.contrib import admin

from .models import ChartData

class ChartDataAdmin(admin.ModelAdmin):
  list_display = [
    'id','user','value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7',
    'value8', 'value9', 'value10', 'value11', 'value12', 'value13', 'value14',
    'value15', 'value16', 'vote_type', 'data'
  ]
  list_filter = ['vote_type', 'data']
  search_fields = ['vote_type']


admin.site.register(ChartData, ChartDataAdmin)