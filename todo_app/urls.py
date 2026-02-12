from django.urls import path

from todo_app.views import (
    TodoListView,
    TagListView
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo_app"
