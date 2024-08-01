from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline']

        labels = {
            'name' : 'Task Name',
            'description' : 'Task Description',
            'deadline' : 'Task DeadLine'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'style': 'height:100px;'}),
            'deadline' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

status_options = [
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('Canceled', 'Canceled'),
    ('Pending', 'Pending'),
]

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline', 'status']

        labels = {
            'name' : 'Task Name',
            'description' : 'Task Description',
            'deadline' : 'Task DeadLine',
            'status' : 'Task Status'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'style': 'height:100px;', 'readonly': True}),
            'deadline' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': True}),
            'status' : forms.RadioSelect(choices=status_options)
        }