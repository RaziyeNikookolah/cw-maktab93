from rest_framework.generics import CreateAPIView
from .serializers import PersonSerializer,EventSerializer,ParticipantShipSerializer
from . import models

class CreatePersonView(CreateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = PersonSerializer
    
class CreateEventView(CreateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = EventSerializer
    
class CreateParticipantShipView(CreateAPIView):
    queryset = models.ParticipantShip.objects.all()
    serializer_class = ParticipantShipSerializer
    
    