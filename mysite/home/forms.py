from django.contrib.auth.models import User
from django import forms
from .models import Titles



class TitlesForm(forms.ModelForm):

    class Meta:
        model = Titles
        fields = ['Title', 'Title_logo']
