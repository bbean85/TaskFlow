from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.home, name='home'),  
    path('login/', views.login_view, name='login'),  
    path('logout/', views.custom_logout_view, name='logout'), 
    path('register/', views.register_view, name='register'), 
    path('tasks/', include('tasks.urls', namespace='tasks')),  
    path('custom-admin/', views.custom_admin_view, name='custom_admin'),  
]
