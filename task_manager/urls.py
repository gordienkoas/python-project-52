from django.conf.urls.i18n import urlpatterns
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]