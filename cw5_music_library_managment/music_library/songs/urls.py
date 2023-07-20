from django.urls import path
from . import views

urlpatterns = [
    path('artists_list/' ,views.display_artists , name= 'display_artists'),
    path('artists_list/<str:genre>' ,views.display_artists_by_genre , name= 'display_artists_by_genre'),
]