from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from statuses.models import Status
from statuses.forms import StatusForm

class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/status_list.html'

class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Статус успешно создан.')
        return super().form_valid(form)

class StatusListView(LoginRequiredMixin, ListView):
     model = Status
     template_name = 'statuses/status_list.html'

class StatusCreateView(LoginRequiredMixin, CreateView):
     model = Status
     form_class = StatusForm
     template_name = 'statuses/status_form.html'

     def form_valid(self, form):
         messages.success(self.request, 'Статус успешно создан.')
         return super().form_valid(form)

     def get_success_url(self):
         return reverse_lazy('status-list')

class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_form.html'
    success_url = reverse_lazy('status-list')

    def form_valid(self, form):
         messages.success(self.request, 'Статус успешно обновлен.')
         return super().form_valid(form)

class StatusDeleteView(LoginRequiredMixin, DeleteView):
     model = Status
     template_name = 'statuses/status_confirm_delete.html'

     def delete(self, request, *args, **kwargs):
         messages.success(self.request, 'Статус успешно удален.')
         return super().delete(request, *args, **kwargs)