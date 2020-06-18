from django.db import models
import datetime
from django.contrib.auth import get_user_model
import django.utils
from django.urls import reverse

OUTCOMES = (
  (1,'SUCCESS'),
  (0, 'FAILURE')
)
PROCEDURES = (
  ('oral_ETT','oral intubation'),
  ('nasal_ETT', 'nasal intubation'),
  ('PICC','PICC placement'),
  ('UAC','Umbilical artery line placement'),
  ('UVC', 'Umbilical vein line placement')
)

# Create your models here.
class Event(models.Model):
  event_user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
  event_name = models.TextField('Select name of event', max_length=10, choices=PROCEDURES)
  event_date = models.DateField('Enter date of event', default=django.utils.timezone.now)
  event_outcome = models.IntegerField('Select outcome',choices=OUTCOMES)

  def __str__(self):
    # return self.event_name
    return f"{self.event_user} did {self.event_name} on {self.event_date}"
    
  # def get_absolute_url(self):
  #   return reverse('event_detail',args=[str(self.id)])
  
  def get_absolute_url(self):
    return reverse('event_list')

    