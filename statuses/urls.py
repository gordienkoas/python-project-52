from django.urls import path
from statuses.views import StatusListView, StatusCreateView, StatusUpdateView, StatusDeleteView


urlpatterns = [
    path('statuses/', StatusListView.as_view(), name='status-list'),
    path('statuses/create/', StatusCreateView.as_view(), name='status-create'),
    path('statuses/<int:pk>/update/', StatusUpdateView.as_view(), name='status-update'),
    path('status/update/<int:pk>/', StatusUpdateView.as_view(), name='status-update'),
    path('statuses/<int:pk>/delete/', StatusDeleteView.as_view(), name='status-delete'),
]