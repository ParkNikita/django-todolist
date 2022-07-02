from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.urls import reverse
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms
# Create your views here.


class SignUpView(CreateView):
    template_name = './registration/signup.html'
    form_class = forms.CustomUserCreationForm

    def get_success_url(self) -> str:
        return reverse('login')

class LandingPage(TemplateView):
    template_name = './landing_page.html'


class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'task_list.html'
    context_object_name = 'tasks'
   
    def get_queryset(self):
        queryset = models.Task.objects.filter(user = self.request.user.id, complete = False)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        queryset = models.Task.objects.filter(
            complete = True,
            user = self.request.user.id
        )
        context.update({
            'completed_tasks': queryset
        })
        return context    


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task_create.html'
    form_class = forms.ModelTaskForm

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return super(TaskCreateView, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse('tasks:task-list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Task
    template_name = 'task_delete.html'

    def get_success_url(self) -> str:
        return reverse('tasks:task-list')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'task_update.html'
    form_class = forms.ModelTaskUpdateForm
    model = models.Task
    
    def get_success_url(self) -> str:
        return reverse('tasks:task-list')