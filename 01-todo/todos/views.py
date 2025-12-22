from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


def home(request):
    todos = Todo.objects.all()
    return render(request, 'todos/home.html', {'todos': todos})


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'TODO created successfully!')
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form, 'action': 'Create'})


def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'TODO updated successfully!')
            return redirect('home')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form, 'action': 'Edit', 'todo': todo})


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'TODO deleted successfully!')
    return redirect('home')


def toggle_resolved(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.is_resolved = not todo.is_resolved
        todo.save()
        status = 'resolved' if todo.is_resolved else 'unresolved'
        messages.success(request, f'TODO marked as {status}!')
    return redirect('home')
