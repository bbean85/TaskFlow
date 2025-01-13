from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser



class Project(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['name']


class Task(models.Model):
    STATUS_CHOICES = [
        ("Incomplete", "Incomplete"),
        ("In Progress", "In Progress"),
        ("Complete", "Complete"),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Incomplete")
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks"
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    project = models.ForeignKey(
        "tasks.Project",
        on_delete=models.CASCADE,
        related_name="tasks",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} - {self.status}"


    def clean(self):
        if self.status == "Complete" and not self.assigned_to:
            raise ValidationError("A completed task must have an assigned user.")

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-created_at']


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
