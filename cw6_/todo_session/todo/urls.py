from django.urls import path
from .views import Create_todo, UpdateTodo, RemoveTodo

app_name = "todo_session"
urlpatterns = [
    path('create/', Create_todo.as_view(), name="create"),
    path('update/', UpdateTodo.as_view(), name="update"),
    path('remove/', RemoveTodo.as_view(), name="remove"),
]
