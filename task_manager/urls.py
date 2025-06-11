from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView
from .views import (
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,
    UserLoginView, register_view,  LabelListView, LabelCreateView,
    LabelUpdateView, LabelDeleteView, StatusListView, StatusCreateView,
    StatusUpdateView, StatusDeleteView, TaskListView, TaskDetailView,
    TaskCreateView, TaskUpdateView, TaskDeleteView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('users/', UserListView.as_view(), name='user-list'),  # Обратите внимание на имя
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('statuses/', StatusListView.as_view(), name='status-list'),
    path('statuses/create/', StatusCreateView.as_view(), name='status-create'),
    path('statuses/<int:pk>/update/', StatusUpdateView.as_view(), name='status-update'),
    path('status/update/<int:pk>/', StatusUpdateView.as_view(), name='status-update'),
    path('statuses/<int:pk>/delete/', StatusDeleteView.as_view(), name='status-delete'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('labels/', LabelListView.as_view(), name='label-list'),
    path('labels/create/', LabelCreateView.as_view(), name='label-create'),
    path('labels/<int:pk>/update/', LabelUpdateView.as_view(), name='label-update'),
    path('labels/<int:pk>/delete/', LabelDeleteView.as_view(), name='label-delete'),
]