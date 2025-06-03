from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import users_view, register_view  # Импорт функций-представлений

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),  # без .as_view()
    path('users/', users_view, name='users'),           # без .as_view()
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]
