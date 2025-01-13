from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'), 
    path('<int:task_id>/', views.task_detail, name='task_detail'),  
    path('create/', views.create_task, name='create'),
    path('<int:task_id>/update/', views.update_task, name='update_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete'),
    path('<int:task_id>/complete/', views.complete_task, name='complete_task'),
    path("mark_complete/<int:task_id>/", views.mark_task_complete, name="mark_complete"),
    path("edit/<int:task_id>/", views.edit_task, name="edit"),
]



