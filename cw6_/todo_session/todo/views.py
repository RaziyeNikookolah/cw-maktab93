from django.shortcuts import render
from django.views import View
from .form import TodoCreateUpdateForm


class Create_todo(View):
    form_class = TodoCreateUpdateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, "todo/create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return render(request, "todo/create.html", {"form": form})


class UpdateTodo(View):
    ...


class RemoveTodo(View):
    ...
