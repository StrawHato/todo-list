from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from todo_app.forms import TaskForm
from todo_app.models import Task, Tag


class TodoListView(generic.ListView):
    model = Task


class TodoCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:todo-list")


class TodoUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:todo-list")


class TodoDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_app:todo-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_app:tag-list")


class ToggleTaskCompleteView(View):
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.status = not task.status
        task.save()
        return redirect("todo_app:todo-list")
