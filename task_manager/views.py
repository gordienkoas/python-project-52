from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

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