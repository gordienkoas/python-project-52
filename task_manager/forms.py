from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Status, Task, Label


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class UserUpdateForm(UserChangeForm):
    password = None  # не показываем поле пароля для редактирования

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'executor', 'labels']