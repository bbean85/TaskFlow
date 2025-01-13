from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Task
from .forms import TaskForm, CustomUserCreationForm


def custom_logout_view(request):
    logout(request)
    return redirect('tasks:task_list')  


@login_required
def task_list(request):
    if request.user.is_staff: 
        tasks = Task.objects.all()
    else:  
        tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.status = "Complete"
        task.save()
        messages.success(request, f"Task '{task.name}' marked as complete.")
    return redirect('tasks:task_list')


@staff_member_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully.")
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})


@staff_member_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect('tasks:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})


@staff_member_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted successfully.")
        return redirect('tasks:task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})




def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("tasks:task_list")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    tasks = Task.objects.all()  
    return render(request, "login.html", {"tasks": tasks})



def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@staff_member_required
def custom_admin_view(request):
    return render(request, 'custom_admin.html', {'message': 'Welcome, Admin!'})

def mark_task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.assigned_to == request.user:  
        task.status = "Complete"
        task.save()
        messages.success(request, f"Task '{task.name}' marked as complete.")
    else:
        messages.error(request, "You are not authorized to modify this task.")
    return redirect('tasks:task_list')
    
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_list")  
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/edit_task.html", {"form": form, "task": task})  

@staff_member_required
def admin_task_list(request):
    tasks = Task.objects.all()
    return render(request, 'admin_task_list.html', {'tasks': tasks})  


def home(request):
    return render(request, 'home.html')
