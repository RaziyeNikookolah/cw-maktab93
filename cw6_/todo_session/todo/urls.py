from django.urls import path
from . import views




urlpatterns = [
    path('create/', Create_todo.as_view(),name="create"),
    path('create/', UpdateTodo.as_view(),name="create"),
    path('create/', RemoveTodo.as_view(),name="create"),
]