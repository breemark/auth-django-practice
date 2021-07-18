from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


# Favorite Color form
class FavColorForm(forms.ModelForm):
    fav_color = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        fields = ('fav_color',)