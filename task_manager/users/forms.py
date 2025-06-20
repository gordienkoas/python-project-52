from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label=_('First name'),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label=_('Last name'),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]
        labels = {
            'username': _('Username'),
            'password1': _('Password'),
            'password2': _('Password confirmation'),
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exclude(
                pk=self.instance.pk).exists():
            raise ValidationError(_('A user with'
                                    ' that username already exists.'))
        return username
# class UserRegisterForm(UserCreationForm):
#     first_name = forms.CharField(
#         label=_("Имя"),
#         max_length=30,
#         widget=forms.TextInput(attrs={'placeholder': 'Имя'}),
#     )
#     last_name = forms.CharField(
#         label=_("Фамилия"),
#         max_length=30,
#         widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}),
#     )
#     username = forms.CharField(
#         label=_("Имя пользователя"),
#         max_length=150,
#         widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
#         help_text=_('Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_')
#     )
#     password1 = forms.CharField(
#         label=_("Пароль"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
#         help_text=_("Ваш пароль должен содержать не менее 3 символов.")
#     )
#     password2 = forms.CharField(
#         label=_("Подтверждение пароля"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля'}),
#         help_text=_("Для подтверждения введите, пожалуйста, пароль ещё раз.")
#     )
#
#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "username", "password1", "password2")
#
#     def clean_password1(self):
#         password1 = self.cleaned_data.get("password1")
#         if len(password1) < 3:
#             raise ValidationError(_("Пароль должен содержать не менее 3 символов."))
#         return password1

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Имя",
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}),
        help_text='Введите ваше имя'
    )
    # last_name = forms.CharField(
    #     label="Фамилия",
    #     max_length=30,
    #     widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}),
    #     help_text='Введите вашу фамилию'
    # )
    # username = forms.CharField(
    #     label="Имя пользователя",
    #     max_length=150,
    #     widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}),
    #     help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_'
    # )

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