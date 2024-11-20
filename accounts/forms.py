from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Admin

class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ('username', 'email', 'first_name', 'last_name')

class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))

    class Meta:
        model = Admin
        fields = ('username', 'password')