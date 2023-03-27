from django.contrib.auth.forms import UserCreationForm
from.models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
    mobile=forms.CharField(widget=forms.TextInput(attrs={'type':'tell','class':'form-control','placeholder':'### ### ####'})) 
    address=forms.CharField(widget=forms.TextInput(attrs={'type':'address','class':'form-control','placeholder':'Enter The Address'})) 
    city=forms.CharField(widget=forms.TextInput(attrs={'type':'address','class':'form-control','placeholder':'Enter City/Town'}))
    state=forms.CharField(widget=forms.TextInput(attrs={'type':'address','class':'form-control','placeholder':'Enter State/Region'}))
    zip=forms.CharField(widget=forms.TextInput(attrs={'type':'zip','class':'form-control','placeholder':'Postal Code'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2','mobile','address','city','state','zip']