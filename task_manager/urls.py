from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from task_manager.views import UserListView, UserLoginView, register_view

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', TemplateView.as_view(template_name='index.html'), name='home'),
     path('users/', include('users.urls')),
     path('login/', UserLoginView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('register/', register_view, name='register'),
]
