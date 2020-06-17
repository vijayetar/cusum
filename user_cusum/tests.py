from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Event

# Create your tests here.
class EventTests(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username = 'tester',
      email='tester@email.com',
      password = 'pass'
    )
    self.event = Event.objects.create(
      event_name = 'PICC',
      event_user = self.user, 
      event_outcome=0,
    )
  
  def test_string_representation(self):
    event = Event(event_name = 'UAC')
    self.assertEqual(str(event), event.event_name)
  
  def test_event_content(self):
    self.assertEqual(f'{self.event.event_name}', 'PICC')
    self.assertEqual(f'{self.event.event_user}', 'tester')
    self.assertEqual(f'{self.event.event_outcome}', 0)
  
  ######## copy from screen shots###############
  # def test_event_list_view(self):
  #   response = self.client.get()