from django import forms
from django.forms import ModelForm
from .models import SDGs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SDGsForm(ModelForm):
     title = forms.CharField(label='Title',widget= forms.TextInput(attrs={'class': 'form-control '}))
     class Meta:
        model = SDGs
        # fields = ['title']
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'image_field'})
        }
        
        labels = {
            'title': '名稱',
            'description': '敘述',
            'slug': '代號',
            'category': '類別',
            'tags': '標籤',
            'image': '圖片'
        }
       
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')