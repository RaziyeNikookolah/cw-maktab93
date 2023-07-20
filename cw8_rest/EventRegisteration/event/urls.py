from django.urls import path
from . import views

urlpatterns = [
    path('person_create/', views.CreatePersonView.as_view(),name="person_create" ),
    path('event_create/', views.CreateEventView.as_view(),name="event_create" ),
    path('ParticipantShip_create/', views.CreateParticipantShipView.as_view(),name="ParticipantShip_create" ),
]