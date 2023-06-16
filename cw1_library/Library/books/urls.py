from . import views
from django.urls import path

urlpatterns = [

    path('books/', views.index, name="index")

]