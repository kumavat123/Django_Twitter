from django import forms
from django.contrib.auth.models import User

from .models import Twitter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TwitterForm(forms.ModelForm):
    class Meta:
        model = Twitter
        fields = ['text','photo']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        # here we are using tuple because it is inbuilt
        fields = ('username', 'email', 'password1', 'password2')

