# integration_hub_app/tests.py
import json
from django.test import TestCase, Client
from django.urls import reverse
from .models import EmailEvent

class ReceiveEventViewTests(TestCase):
  def setUp(self):
      self.client = Client()

  def test_receive_event_post(self):
      url = reverse('receive_event')
      data = {
          'customer_id': '123',
          'event_type': 'email_click',
          'email_id': '456',
          'timestamp': '2023-01-01T12:00:00',
          'clicked_link': 'https://example.com'
      }
      response = self.client.post(url, json.dumps(data), content_type='application/json')
      
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.json(), {'message': 'Event received and saved successfully'})

      email_events = EmailEvent.objects.filter(customer_id='123', event_type='email_click')
      self.assertEqual(email_events.count(), 1)
      self.assertEqual(email_events[0].event_data['email_id'], '456')

  def test_get_events(self):
      EmailEvent.objects.create(
          customer_id='123',
          event_type='email_open',
          event_data={'email_id': '789', 'timestamp': '2023-01-02T12:00:00'}
      )

      url = reverse('get_events', kwargs={'customer_id': '123'})
      response = self.client.get(url)

      self.assertEqual(response.status_code, 200)
      self.assertEqual(len(response.json()['events']), 1)
      self.assertEqual(response.json()['events'][0]['customer_id'], '123')

