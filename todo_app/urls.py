from django.urls import path

from todo_app.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TagListView,
    toggle_complete_task,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
    path("create/", TodoCreateView.as_view(), name="task-create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("<int:pk>/toggle-complete/", toggle_complete_task, name="toggle-complete"),
]

app_name = "todo_app"
