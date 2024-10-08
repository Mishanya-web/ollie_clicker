from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={
                                   'type': 'text',
                                   'id': 'field1',
                                   'placeholder': 'login',
                               }))
    password = forms.CharField(label='',
                               widget=forms.TextInput(attrs={
                                   'type': 'password',
                                   'id': 'field2',
                                   'placeholder': 'password',
                               }))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={
                                   'type': 'text',
                                   'id': 'field1',
                                   'placeholder': 'login',

                               }))

    password1 = forms.CharField(label='',
                                widget=forms.TextInput(attrs={
                                   'type': 'password',
                                   'id': 'field2',
                                   'placeholder': 'password',
                                }))

    password2 = forms.CharField(label='',
                                widget=forms.TextInput(attrs={
                                   'type': 'password',
                                   'id': 'field3',
                                   'placeholder': 'password',
                                }))