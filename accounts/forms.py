from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class registerUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', )
        