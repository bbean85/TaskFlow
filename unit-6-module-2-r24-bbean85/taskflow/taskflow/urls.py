from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.custom_logout_view, name='logout'),
    path('auth/register/', views.register_view, name='register'),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('auth/', include('django.contrib.auth.urls'))
]


