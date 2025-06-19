from django.urls import path
from task_manager.labels.views import LabelListView, LabelCreateView, LabelUpdateView, LabelDeleteView


urlpatterns = [
    path('labels/', LabelListView.as_view(), name='label-list'),
    path('labels/create/', LabelCreateView.as_view(), name='label-create'),
    path('labels/<int:pk>/update/', LabelUpdateView.as_view(), name='label-update'),
    path('labels/<int:pk>/delete/', LabelDeleteView.as_view(), name='label-delete'),
]