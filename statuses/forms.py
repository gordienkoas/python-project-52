from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from statuses.models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


