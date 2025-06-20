from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import re


class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Имя',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Имя'})
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Фамилия'})
    )
    username = forms.CharField(
        label='Имя пользователя',
        max_length=150,
        required=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'})
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
        help_text='Ваш пароль должен содержать как минимум 3 символа.',
        min_length=3
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 150:
            raise forms.ValidationError('Логин не должен превышать 150 символов.')
        # Проверка допустимых символов
        if not re.match(r'^[\w.@+-]+$', username):
            raise forms.ValidationError('Допустимы только буквы, цифры и символы @/./+/-/_.')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if len(password1) < 3:
            raise forms.ValidationError('Пароль должен содержать минимум 3 символа.')

        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают.')

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

# class UserRegisterForm(UserCreationForm):
#     first_name = forms.CharField(
#         label=_("Имя"),
#         max_length=30,
#         required=True,
#         widget=forms.TextInput(attrs={'placeholder': 'Имя'}),
#     )
#     last_name = forms.CharField(
#         label=_("Фамилия"),
#         max_length=30,
#         required=True,
#         widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}),
#     )
#     # остальные поля ...
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         if commit:
#             user.save()
#         return user



class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Имя",
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}),
        help_text='Введите ваше имя'
    )
    last_name = forms.CharField(
        label="Фамилия",
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}),
        help_text='Введите вашу фамилию'
    )
    username = forms.CharField(
        label="Имя пользователя",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}),
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_'
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username")

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'placeholder': 'Введите имя пользователя'
        })
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введите пароль'
        }),
    )