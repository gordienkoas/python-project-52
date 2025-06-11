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
from .forms import UserRegisterForm, UserUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Status, Task, Label
from .forms import StatusForm, TaskForm, LabelForm
from .filters import TaskFilter
from django_filters.views import FilterView


def home_view(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # После регистрации перенаправляем на вход
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def users_view(request):
    # Страница со списком пользователей (требует авторизации)
    from django.contrib.auth.models import User
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
    else:
        form = AuthenticationForm()
    # Добавляем класс 'form-control' к каждому полю
    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control'})

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    return render(request, 'login.html', {'form': form})

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

# Создание пользователя (регистрация)
class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('login')  # после регистрации — вход

# Редактирование пользователя — только сам пользователь
class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

# Удаление пользователя — только сам пользователь
class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

# Вход
class UserLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')  # замените на ваш URL главной страницы

# Выход
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

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


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Задача успешно создана.')
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        messages.success(self.request, 'Задача успешно обновлена.')
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.author

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.author

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Задача успешно удалена.')
        return super().delete(request, *args, **kwargs)


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('label-list')
    success_message = "Метка успешно создана"


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


class TaskListView(FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10  # если нужна пагинация

    def get_filterset(self, filterset_class):
        # Передаём request в фильтр, чтобы использовать self.request.user
        return filterset_class(self.request.GET, queryset=self.get_queryset(), request=self.request)

    def get_queryset(self):
        return Task.objects.all().order_by('id')