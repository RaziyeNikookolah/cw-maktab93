from models import TodoModel
from django import forms


class createForm(forms.Form):
    class Meta:
        model = TodoModel
        fields = ('title', 'description')
