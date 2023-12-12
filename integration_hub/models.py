from django.db import models

class EmailEvent(models.Model):

  CUSTOMER_ACTIONS = [
    ('email_open', 'Email Open'),
    ('email_click', 'Email Click'),
    ('email_unsubscribe', 'Email Unsubscribe'),
    ('purchase', 'Purchase'),
  ]
  customer_id = models.CharField(max_length=255)
  event_type = models.CharField(max_length=20, choices=CUSTOMER_ACTIONS)
  event_data = models.JSONField()
  timestamp = models.DateTimeField(auto_now_add=True)
