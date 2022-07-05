from django.db import models
from django import forms
from .models import Register
from .models import Login
from user.models import User

class RegisterF(forms.ModelForm):
    class Meta:
        model=User
        # fields='__all__'
        fields=['username','first_name','last_name','email','password']

        widgets = {
            'username': forms.TextInput(attrs={"placeholder":"Enter Username"}),
            'first_name':forms.TextInput(attrs={"placeholder":"Enter Your First Name"}),
            'last_name':forms.TextInput(attrs={"placeholder":"Enter Your Last Name"}),
            'email':forms.EmailInput(attrs={"placeholder":"Enter Your Email address"}),
            'password':forms.PasswordInput(attrs={"placeholder":"Enter Password"}),
            
            }

class LoginF(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
        widgets={
            'username':forms.TextInput(attrs={"placeholder":"Enter Your Username"}),
            'password':forms.PasswordInput(attrs={"placeholder":"Enter Your Password"})
        }