import django_filters
from django import forms
from django.contrib.auth import get_user_model
from .models import Task, Label

User = get_user_model()

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(label='Статус', empty_label='Любой')
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Исполнитель',
        empty_label='Любой',
    )
    labels = django_filters.ModelMultipleChoiceFilter(
        queryset=Label.objects.all(),
        label='Метки',
        widget=forms.CheckboxSelectMultiple,
    )
    author = django_filters.BooleanFilter(
        method='filter_author',
        label='Только мои задачи',
        widget=forms.CheckboxInput,
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        statuses = Task.objects.values_list('status', flat=True).distinct()
        choices = [(status, status) for status in statuses if status]
        self.filters['status'].extra['choices'] = choices

    def filter_author(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
