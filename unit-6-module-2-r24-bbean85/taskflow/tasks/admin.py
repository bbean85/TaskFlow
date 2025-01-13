from django.contrib import admin
from .models import Project, Task, CustomUser


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1
    fields = ('name', 'status')
    readonly_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)
    inlines = [TaskInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'created_at')
    list_editable = ('status',)
    search_fields = ('name', 'status')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    readonly_fields = ('is_staff',)


# Customize Admin Panel
admin.site.site_header = "TaskFlow Admin"
admin.site.site_title = "TaskFlow Admin Portal"
admin.site.index_title = "Welcome to the TaskFlow Admin Panel"
