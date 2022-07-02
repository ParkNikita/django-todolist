from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

from . import models

class ModelTaskForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = (
            'title',
            'description',
        )


class ModelTaskUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = (
            'title',
            'description',
            'complete'
        )    


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = models.User
        fields = ("username",)
        field_classes = {"username": UsernameField}

