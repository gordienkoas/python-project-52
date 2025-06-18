from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
#from task_manager.forms import UserRegisterForm, UserUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
#from task_manager.models import Status, Task, Label
#from task_manager.forms import StatusForm, TaskForm, LabelForm
#from task_manager.filters import TaskFilter
from django_filters.views import FilterView
#
#
# def home_view(request):
#     return render(request, 'index.html')
#
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # После регистрации перенаправляем на вход
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
#
# @login_required
# def users_view(request):
#     # Страница со списком пользователей (требует авторизации)
#     from django.contrib.auth.models import User
#     users = User.objects.all()
#     return render(request, 'users.html', {'users': users})
#
#
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#     else:
#         form = AuthenticationForm()
#     # Добавляем класс 'form-control' к каждому полю
#     for field in form.fields.values():
#         field.widget.attrs.update({'class': 'form-control'})
#
#     if request.method == 'POST' and form.is_valid():
#         user = form.get_user()
#         login(request, user)
#         return redirect('home')
#     return render(request, 'login.html', {'form': form})
#
class UserListView(ListView):
     model = User
     template_name = 'users/user_list.html'
     context_object_name = 'users'
#
# # Создание пользователя (регистрация)
# class UserCreateView(CreateView):
#     model = User
#     form_class = UserRegisterForm
#     template_name = 'users/user_form.html'
#     success_url = reverse_lazy('login')  # после регистрации — вход
#
# # Редактирование пользователя — только сам пользователь
# class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = User
#     form_class = UserUpdateForm
#     template_name = 'users/user_form.html'
#     success_url = reverse_lazy('user-list')
#
#     def test_func(self):
#         user = self.get_object()
#         return self.request.user == user # Редактирование пользователя — только сам пользователь
# class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = User
#     form_class = UserUpdateForm
#     template_name = 'users/user_form.html'
#     success_url = reverse_lazy('user-list')
#
#     def test_func(self):
#         user = self.get_object()
#         return self.request.user == user
#
# # Удаление пользователя — только сам пользователь
# class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = User
#     template_name = 'users/user_confirm_delete.html'
#     success_url = reverse_lazy('user-list')
#
#     def test_func(self):
#         user = self.get_object()
#         return self.request.user == user
#
# # Вход
class UserLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')  # замените на ваш URL главной страницы
#
# # Выход
# class UserLogoutView(LogoutView):
#     next_page = reverse_lazy('login')
#
#
#
#
#
#
#
#
# class TaskListView(FilterView):
#     model = Task
#     filterset_class = TaskFilter
#     template_name = 'tasks/task_list.html'
#     context_object_name = 'tasks'
#     paginate_by = 10  # если нужна пагинация
#
#     def get_filterset(self, filterset_class):
#         # Передаём request в фильтр, чтобы использовать self.request.user
#         return filterset_class(self.request.GET, queryset=self.get_queryset(), request=self.request)
#
#     def get_queryset(self):
#         return Task.objects.all().order_by('id')