from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    executor = models.ForeignKey(  # Изменили название поля
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='executed_tasks'
    )
    labels = models.ManyToManyField(Label, blank=True, related_name='tasks')
    status = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')
    created_at = models.DateTimeField(auto_now_add=True)


