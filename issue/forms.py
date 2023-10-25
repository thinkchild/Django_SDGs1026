from django import forms
from .models import ChartData

class ChartDataForm(forms.ModelForm):
    class Meta:
        model = ChartData
        fields = ['value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', 'value8', 'value9', 'value10', 'value11', 'value12', 'value13', 'value14', 'value15', 'value16', 'vote_type']
        # 将投票类型添加到字段中

class ChartDataFormVote02(forms.ModelForm):
    class Meta:
        model = ChartData
        fields = ['value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', 'value8', 'value9', 'value10', 'value11', 'value12', 'value13', 'value14', 'value15', 'value16', 'vote_type']
        # 将投票类型添加到字段中，你可以根据需要添加其他字段
