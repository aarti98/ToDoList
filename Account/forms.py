from django.forms import models
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSignUpForm(models.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class':'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'class':'form-control'
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control'
        })


class UserLoginForm(models.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__()
        self.fields['username'].widget.attrs.update({
            'placeholder':'UserName',
            'class':'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder':'Password',
            'class':'form-control'
        })
