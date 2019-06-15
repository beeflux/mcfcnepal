from django.shortcuts import render
from .models import Events
from django.views.generic import CreateView, ListView, DetailView
from .forms import EventAddForm
from datetime import date, datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

class EventAddView(CreateView):
    model = Events
    form_class = EventAddForm
    template_name = 'events/index.html'
    success_url = 'events'

class EventListView(ListView):
    model = Events
    template_name = "events/events.html"
    context_object_name = "events"
    def get_queryset(self):
        events = Events.upcoming_events.all()
        return events
    

class PastEventListView(ListView):
    model = Events
    template_name = "events/pastevent.html"
    context_object_name = "past_events"
    def get_queryset(self):
        past_events = Events.past_events.all()
        return past_events


class EventDetailView(DetailView):
    model = Events
    template_name = 'events/events-detail.html'

class PastEventDetailView(DetailView):
    model = Events
    template_name = 'events/past-event-detail.html'