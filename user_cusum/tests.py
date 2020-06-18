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
      event_date = '2020-06-16',
      event_outcome=0,
    )
  
  def test_string_representation(self):
    event = Event(event_name='UAC', event_user=self.user, event_date='2020-06-16', event_outcome=1)
    self.assertEqual(str(event), f"{event.event_user} did {event.event_name} on {event.event_date}",)
  
  #test content of the database
  def test_event_content(self):
    self.assertEqual(f'{self.event.event_name}', 'PICC')
    self.assertEqual(f'{self.event.event_user}', 'tester')
    self.assertEqual(f'{self.event.event_outcome}', '0')
  
  #test list view on url event_list
  def test_event_list_view(self):
    response = self.client.get(reverse('event_list'))
    self.assertEqual(response.status_code,200)
    self.assertTemplateUsed(response, 'event_list.html')
    self.assertContains(response, 'PICC')

  #test detail view on url event_detail
  def test_event_detail_view(self):
    response = self.client.get(reverse('event_detail', args='1'))
    self.assertEqual(response.status_code,200)
    no_response = self.client.get(reverse('event_detail', args='9'))
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response, 'PICC')
    self.assertTemplateUsed(response, 'event_detail.html')

  #test create view on url event_create
  def test_event_create_view(self):
    response = self.client.post(reverse('event_create'), {'event_name': 'UAC',
      'event_user': self.user, 
      'event_date': '2020-06-15',
      'event_outcome': 0,
    })
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'UAC')
    self.assertContains(response, 0)
    self.assertTemplateUsed(response, 'event_create.html')
  
  #test update view on url event_update
  def test_event_update_view(self):
    response = self.client.post(reverse('event_update',args = '1'), {
      'event_name':'UVC',
      'event_outcome':1,
      'event_date':'2019-06-16'
    })
    self.assertEqual(response.status_code, 302)

  #test delete view on url event_delete
  def test_event_delete_view(self):
    response = self.client.get(reverse('event_delete', args='1'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Delete')
    self.assertTemplateUsed(response, 'event_delete.html')
