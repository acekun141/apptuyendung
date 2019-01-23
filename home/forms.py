from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
import re

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder':'Tài khoản'})
    )
    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder':'Mật khẩu'})
    )
    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder':'Nhập lại mật khẩu'})
    )

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if not( password1 == password2 ):
                raise forms.ValidationError('Mật khẩu không hợp lệ!')
            if len(password1) < 6:
                raise forms.ValidationError('Mật khẩu quá ngắn')
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Tài khoản có chứa kí tự đặc biệt!')
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Tài khoản đã tồn tại')
    def save(self):
        User.objects.create_user(
            username = self.cleaned_data['username'],
            password = self.cleaned_data['password1']
        )

class SigninForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder':'Tài khoản'})
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={'placeholder':'Mật khẩu'})
    )
    def clean(self):
        user = authenticate(username = self.cleaned_data['username'], password = self.cleaned_data['password'])
        if not user:
            raise forms.ValidationError('Mật khẩu hoặc tài khoản không đúng')