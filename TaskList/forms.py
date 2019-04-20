from django.forms import ModelForm
from .models import ToDoList


class AddTaskForm(ModelForm):
    class Meta:
        model  = ToDoList
        fields = ['title', 'description', 'created_date', 'due_date', 'completed', 'Author']


class UpdateTaskForm(ModelForm):
    class Meta:
        model  = ToDoList
        fields = ['title', 'description', 'due_date', 'completed']