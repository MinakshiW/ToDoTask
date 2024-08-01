from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from datetime import datetime

# Create your views here.
def homeview(request):
    return  render(request, 'app1/home.html', {})

def formview(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/form.html', {'form': form})

def showview(request):
    obj = Task.objects.all()
    return render(request, 'app1/show.html', {'obj': obj})

def updateview(request, pk):
    obj = Task.objects.get(id=pk)
    form = TaskForm(instance=obj)
    if request.method == 'POST':
        s = request.POST.get('status')
        obj.status = s
        form = TaskForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/update.html', {'form': form})

def deleteview(request, x):
    obj = Task.objects.get(id=x)
    if request.method == 'POST':
        obj.delete()
        return redirect('/a1/sv/')
    return render(request, 'app1/success.html', {'obj': obj})