from rest_framework import serializers
from .models import Event, Participant

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

    def validate(self, data):
        # myvalue = dict['mickey']
        event = data['event']
        if event.participants.all().count() >= event.max_participants:
            raise serializers.ValidationError("Maximum de personnes atteint.") 
        return data

