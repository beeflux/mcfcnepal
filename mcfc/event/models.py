from django.db import models
from django import forms
from datetime import date, timezone
# Create your models here.
class EventpastManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(start_date__lt=date.today())

class EventupcomingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(start_date__gte=date.today())


class Events(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    title =  models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='events/images', default="events/images/events.png")
    last_modified = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    past_events = EventpastManager()
    objects = EventupcomingManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'events'
        
        
