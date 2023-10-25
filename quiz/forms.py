# quiz_app/forms.py
from django import forms

class AnswerForm(forms.Form):
    user_answer = forms.ChoiceField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], widget=forms.RadioSelect)
