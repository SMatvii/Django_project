from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from serializers import CaptchaFieldSerializer

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True) 
    
    class Meta:
        model = User
        extra_fields = ['email']
        fields = ['username', 'password1','passworrd2']

class ProfileUpdateForm(forms.Form):
    email = forms.EmailField(required=True, label="Email:")
    avatar = forms.ImageField(required=False, label="Upload avatar:")
    
    def clean_email(self):
        new_email = self.cleaned_data.get("email")
        if User.objects.filter(email=new_email).exists():
            raise ValidationError("This email already exsist")
        else:
            ("new_email")
            
def __init__(self, *args, **kwargs):
    self.user = kwargs.pop("user", None)
    super().__init__(**args, **kwargs)
    if self.user:
        self.fields["email"].initial = self.user.email


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Login:')
    password = forms.PasswordInput()