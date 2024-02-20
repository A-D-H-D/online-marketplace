from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget= forms.TextInput(attrs={
        'placeholder':'Username',
        'class':'w-full py-4 px-6 my-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-blue-500'
    }))   
    
    email = forms.CharField(widget= forms.EmailInput(attrs={
        'placeholder':'Email address',
        'class':'w-full py-4 px-6 my-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-blue-500'
    }))

    password1 = forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'w-full py-4 px-6 my-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-blue-500'
    }))    

    password2 = forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Confirm password',
        'class':'w-full py-4 px-6 my-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-blue-500'
    }))    

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={
        'placeholder':'Username',
        'class':'w-full py-4 px-6 my-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-blue-500'
    })) 
        
    password = forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'w-full py-4 px-6 my-4 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-blue-500'
    }))      