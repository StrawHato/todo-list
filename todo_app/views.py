from django.shortcuts import render
from django.views import generic

from todo_app.models import Task, Tag


class TodoListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag
