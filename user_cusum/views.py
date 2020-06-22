from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Event
from django.urls import reverse_lazy

# Create your views here.

class EventListView(ListView):
  template_name = 'event_list.html'
  model = Event

class EventDetailView(DetailView):
  template_name = 'event_detail.html'
  model = Event

class EventCreateView(CreateView):
  template_name = 'event_create.html'
  model = Event
  fields = ['event_name', 'event_user', 'event_date', 'event_outcome']

class EventUpdateView(UpdateView):
  template_name = 'event_update.html'
  model = Event
  fields = ['event_name','event_date', 'event_outcome']

class EventDeleteView(DeleteView):
  template_name = 'event_delete.html'
  model = Event
  success_url = reverse_lazy('event_list')

class AboutViewPage(TemplateView):
  template_name = 'about.html'
