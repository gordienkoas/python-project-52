# from django.shortcuts import render
from .models import Label
from .forms import CreateLabelForm

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect


class LabelView(ListView):
    model = Label
    context_object_name = "label_list"
    template_name = "labels/label_list.html"


class CreateLabelView(SuccessMessageMixin, CreateView):
    template_name = "labels/create.html"
    success_url = reverse_lazy("labels:label_list")
    form_class = CreateLabelForm
    success_message = _("Label created successfully")


class UpdateLabelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    success_url = reverse_lazy("labels:label_list")
    template_name = "labels/update.html"
    form_class = CreateLabelForm
    success_message = _("Label updated successfully")
    login_url = reverse_lazy("labels:label_list")
    redirect_field_name = None


class DeleteLabelView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    success_url = reverse_lazy("labels:label_list")
    template_name = "labels/delete.html"
    success_message = _("Label deleted successfully")
    login_url = reverse_lazy("login")
    redirect_field_name = None

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(request, self.success_message)
            return response
        except ProtectedError:
            messages.error(request, _("Невозможно удалить метку"))
            return redirect(self.success_url)