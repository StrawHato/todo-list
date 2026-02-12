from django.urls import path

from todo_app.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TagListView,
    toggle_complete_task,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
    path("create/", TodoCreateView.as_view(), name="task-create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("<int:pk>/toggle-complete/", toggle_complete_task, name="toggle-complete"),
]

app_name = "todo_app"
