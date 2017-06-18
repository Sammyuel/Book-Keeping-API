from django.contrib.auth.models import User
from django import forms
from .models import Posts
from home.models import Titles

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['team_1', 'team_2', 'bet_ammount', 'receive_ammount','result']
