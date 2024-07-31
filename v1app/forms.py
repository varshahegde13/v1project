from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    model = User
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
class SearchForm(forms.Form):
    username = forms.CharField(max_length=150, required=False)
