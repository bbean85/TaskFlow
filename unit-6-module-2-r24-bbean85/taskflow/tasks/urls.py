from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required


app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),  
    path('<int:task_id>/', views.task_detail, name='task_detail'),  
    path('new/', views.create_task, name='create_task'),  
    path('create/', staff_member_required(views.create_task), name='create_task'),
    path('<int:task_id>/update/', staff_member_required(views.update_task), name='update_task'),
    path('<int:task_id>/delete/', staff_member_required(views.delete_task), name='delete_task'),
    path('<int:task_id>/complete/', views.complete_task, name='complete_task'),
]
