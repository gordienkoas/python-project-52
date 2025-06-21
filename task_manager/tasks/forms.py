from django.forms import ModelForm
from .models import Task
from django import forms
from django.utils.translation import gettext_lazy as _

DATA = {
    "tasks": {
        "first": {
            "executor": "Выберите исполнителя"
        }
    }
}

class CreateTaskForm(ModelForm):
    description = forms.CharField(
        label=_("Task description"),
        widget=forms.Textarea(
            attrs={"style": "height: 13em; resize: none;"},
        ),
    )

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if 'executor' in form.fields:
            choices = list(form.fields['executor'].choices)
            choices.append(('special_value', DATA["tasks"]["first"]["executor"]))
            form.fields['executor'].choices = choices
        return form

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "status",
            "executor",
            "labels",
        )