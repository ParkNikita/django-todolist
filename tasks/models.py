from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True, null=True)
    complete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']