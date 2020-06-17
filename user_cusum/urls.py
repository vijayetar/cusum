from django.urls import path
from .views import EventListView, EventDetailView

urlpatterns = [
  path("", EventListView.as_view(), name = 'event_list'),
  path("event_detail/<int:pk>", EventDetailView.as_view(), name = 'event_detail')
]
