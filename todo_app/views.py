from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from todo_app.models import Task, Tag


class TodoListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag


def toggle_complete_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.status:
        task.status = False
    else:
        task.status = True
    task.save()
    return redirect("todo_app:todo-list")
