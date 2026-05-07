from django.shortcuts import render, get_object_or_404, redirect

from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    latest_task_list = Task.objects.order_by('created_at')[:5]
    context = {'latest_task_list': latest_task_list}
    return render(request, 'tasks/index.html', context)


def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')
    return render(request, 'tasks/delete_task.html', {'task': task})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'tasks/add_task.html', context)