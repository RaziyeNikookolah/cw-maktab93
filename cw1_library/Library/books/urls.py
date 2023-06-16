from . import views
from django.urls import path

path('books/', views.index, name="index")
