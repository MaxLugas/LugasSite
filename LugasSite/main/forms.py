from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import  TextInput, EmailInput, PasswordInput, CharField

class RegisterUserForm(UserCreationForm):
    username= CharField(widget=TextInput(attrs={'class': 'form-control'}))
    email = CharField(widget=EmailInput(attrs={'class': 'form-control'}))
    password1 = CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(label='Confirm password', widget=PasswordInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm password'
            }),
        }
