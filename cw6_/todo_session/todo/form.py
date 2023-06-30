from .models import TodoModel
from django import forms


class TodoCreateUpdateForm(forms.Form):
    class Meta:
        model = TodoModel
        fields = ('title', 'description')
