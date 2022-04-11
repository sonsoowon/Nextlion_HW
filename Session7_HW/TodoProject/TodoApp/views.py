from ast import arg
from re import template
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
    todo_list = Todo.objects.all()
    return render(request, 'index.html', {'todo_list':todo_list})

def add(request):
    if request.method == "POST":
        todo = Todo.objects.create(
            title = request.POST['title'],
            deadline = request.POST['deadline'],
            content = request.POST['content']
        )
        
        return redirect('index')
    
    return render(request, 'add.html')

def detail(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo_deadline = todo.deadline.strftime('%Y-%m-%d')
    
    return render(request, 'detail.html', {
        'todo':todo,
        'todo_deadline': todo_deadline})

def edit(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo_deadline = todo.deadline.strftime('%Y-%m-%d')
    if request.method == "POST":
        todo = Todo.objects.filter(pk=todo_id).update(
            title = request.POST['title'],
            deadline = request.POST['deadline'],
            content = request.POST['content']
        )
        return redirect('index')

    return render(request, 'edit.html', {
        'todo': todo,
        'todo_deadline': todo_deadline})

def delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()

    return redirect('index')
