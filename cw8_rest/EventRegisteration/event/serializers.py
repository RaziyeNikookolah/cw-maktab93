from rest_framework import serializers
from .models import Person, Event, ParticipantShip


class ParticipantShipSerializer(serializers.ModelSerializer):
    # registered_event = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = ParticipantShip
        fields = ('person','event')
        # read_only_fields=('registered_event',)

class PersonSerializer(serializers.ModelSerializer):
    # 
    class Meta:
        model = Person
        fields = "__all__"
        # depth=1
       


class EventSerializer(serializers.ModelSerializer):
    # participantShips = ParticipantShipSerializer(many=True)
    class Meta:
        model = Event
        fields = "__all__"
        # depth=1

