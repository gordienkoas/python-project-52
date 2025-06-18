from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Label
from .forms import LabelForm
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'

class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('label-list')

    def form_valid(self, form):
        messages.success(self.request, "Метка успешно создана")
        return super().form_valid(form)


# class LabelListView(LoginRequiredMixin, ListView):
#     model = Label
#     template_name = 'labels/label_list.html'
#     context_object_name = 'labels'


# class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = Label
#     form_class = LabelForm
#     template_name = 'labels/label_form.html'
#     success_url = reverse_lazy('label-list')
#     success_message = "Метка успешно создана"


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('label-list')
    success_message = "Метка успешно изменена"


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/label_confirm_delete.html'
    success_url = reverse_lazy('label-list')

    def form_valid(self, form):
        if self.object.tasks.exists():
            messages.error(self.request, "Нельзя удалить метку, связанную с задачами")
            return redirect(reverse('label-list'))
        messages.success(self.request, "Метка успешно удалена")
        return super().form_valid(form)
