from django.contrib import admin
from django.urls import path, include
from task_manager import views
from .users.views import LoginUserView, LogoutAllowGetView
# from django.conf import settings
# from django.conf.urls.static import static
from django.views.i18n import set_language

app_name = "task_manager"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("login/", LoginUserView.as_view(), name="login"),
    path('logout/', LogoutAllowGetView.as_view(next_page='/'), name='logout'),
    path("users/", include("task_manager.users.urls"), name="users"),
    path("statuses/", include("task_manager.statuses.urls"), name="statuses"),
    path("tasks/", include("task_manager.tasks.urls"), name="tasks"),
    path("labels/", include("task_manager.labels.urls"), name="labels"),
    path('i18n/setlang/', set_language, name='set_language'),
]