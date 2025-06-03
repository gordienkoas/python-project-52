from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

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
