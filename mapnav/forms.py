from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper


class signupform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'username'}),label='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'first name'}),label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'last name'}),label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={ 'placeholder':'email'}),label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'password'}),label='')
    password2= forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'confirm password'}),label='')

    class Meta:
        model=User
        fields=('username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',)
    def save(self,commit=True):
        user=super(signupform,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user




