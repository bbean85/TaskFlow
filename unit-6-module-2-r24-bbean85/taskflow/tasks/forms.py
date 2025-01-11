from django import forms
from .models import Project, Task, CustomUser
from django.contrib.auth.forms import UserCreationForm

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']  

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description',]
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
