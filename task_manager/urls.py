from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView
from .views import (
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,
    UserLoginView, register_view
)
from .views import (StatusListView, StatusCreateView,
                    StatusUpdateView, StatusDeleteView)

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
]



# from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from django.views.generic import TemplateView
# from .views import users_view, register_view  # Импорт функций-представлений
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('register/', register_view, name='register'),  # без .as_view()
#     path('users/', users_view, name='users'),           # без .as_view()
#     path('', TemplateView.as_view(template_name='index.html'), name='home'),
# ]
