from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EventSerializer, ParticipantSerializer
from .models import Event, Participant

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer