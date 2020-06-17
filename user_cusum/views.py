from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import Event

# Create your views here.

class EventListView(ListView):
  template_name = 'event_list.html'
  model = Event

class EventDetailView(DetailView):
  template_name = 'event_detail.html'
  model = Event

# class EventCreateView(CreateView):
#   template_name = 'event_create.html'
#   model = Event
#   fields = ['event_name', 'event_outcome']