from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')