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