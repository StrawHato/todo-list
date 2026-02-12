from django.urls import path

from todo_app.views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
]

app_name = "todo_app"
