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
            'name': 'first_name'  # добавляем name для поиска в тесте
        }),
    )
    last_name = forms.CharField(
        label=_("Фамилия"),
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Фамилия',
            'name': 'last_name'
        }),
    )
    username = forms.CharField(
        label=_("Имя пользователя"),
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя пользователя',
            'name': 'username'
        }),
        help_text=_('Обязательное поле. Не более 150 символов.')
    )
    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'name': 'password1'
        }),
        help_text=_("Ваш пароль должен содержать не менее 3 символов.")
    )
    password2 = forms.CharField(
        label=_("Подтверждение пароля"),
        strip=False,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Подтверждение пароля',
            'name': 'password2'
        }),
        help_text=_("Для подтверждения введите, пожалуйста, пароль ещё раз.")
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 3:
            raise ValidationError(_("Пароль должен содержать не менее 3 символов."))
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Пароли не совпадают."))

        return cleaned_data


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