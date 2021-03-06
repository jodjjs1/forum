from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from langdetect import detect

class UserRegData(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Фамилия')
    login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Логин')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Email')
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Пароль')

    def clean_login(self):
        data = self.cleaned_data['login']

        if len(data) > 15:
            raise ValidationError(_('Много буков (>15)'), code='invalid')
        if detect(data) == 'ru':
            print(detect(data))
            raise ValidationError(_('Login errror'))

        return data

    def clean_password(self):
        data = self.cleaned_data['password']

        if len(data) < 8:
            raise ValidationError(_('Слишком короткий пароль(меньше 8 символов'))

        return data

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        return data[0].upper() + data[1:].lower()

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        return data[0].upper() + data[1:].lower()


class UserLogData(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Логин')
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Пароль')
