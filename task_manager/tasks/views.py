from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _

from django_filters.views import FilterView

from .forms import CreateTaskForm
from .models import Task
from .filters import TaskFilter
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages


class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasks/task_list.html"
    filterset_class = TaskFilter


class CreatTaskView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = "tasks/create.html"
    success_url = reverse_lazy("tasks:task_list")
    form_class = CreateTaskForm
    success_message = _("Task created successfully")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class DetailTaskView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"




# class DeleteTaskView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
#     pattern_name = "tasks:list"
#     model = Task
#     success_url = reverse_lazy("tasks:task_list")
#     template_name = "tasks/delete.html"
#     success_message = _("Task deleted successfully")
#     login_url = reverse_lazy("login")
#     redirect_field_name = None
class DeleteTaskView(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    redirect_field_name = None
    success_url = reverse_lazy("tasks:task_list")
    permission_denied_url = reverse_lazy("tasks:task_list")

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)

        # Проверка, что текущий пользователь — автор задачи
        if task.author != request.user:
            messages.error(request, _("Only the task's author can delete it"))
            return redirect(self.permission_denied_url)

        task.delete()
        messages.success(request, _("Task was deleted successfully"))
        return redirect(self.success_url)


class UpdateTaskView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    success_url = reverse_lazy("tasks:task_list")
    template_name = "tasks/update.html"
    form_class = CreateTaskForm
    success_message = _("Task updated successfully")
    # login_url = reverse_lazy("tasks:task_list")
    # redirect_field_name = None