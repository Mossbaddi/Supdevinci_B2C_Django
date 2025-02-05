from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    max_participants = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name
    


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name