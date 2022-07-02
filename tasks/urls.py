from django.contrib import admin
from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name = 'task-list'),
    path('create/', views.TaskCreateView.as_view(), name = 'task-create'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name = 'task-delete'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name = 'task-update'),

]
