from django.db import models


class TodoModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
