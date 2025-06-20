from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label=_("Имя"),
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя',
            # 'name': 'first_name'  # обычно не обязательно добавлять вручную
        }),
    )
    last_name = forms.CharField(
        label=_("Фамилия"),
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Фамилия',
        }),
    )
    username = forms.CharField(
        label=_("Имя пользователя"),
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя пользователя',
        }),
    )
    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
        }),
    )
    password2 = forms.CharField(
        label=_("Подтверждение пароля"),
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Подтверждение пароля',
        }),
    )


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