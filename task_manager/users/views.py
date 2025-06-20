from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from task_manager.users.forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # или куда нужно
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

class UserLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')  # замените на ваш URL главной страницы


# Создание пользователя (регистрация)
class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('login')


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        user = self.get_object()
        return self.request.user == user