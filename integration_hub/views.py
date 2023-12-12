from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EmailEvent
import json

@csrf_exempt
def receive_event(request):
    if request.method == 'POST':
        # Process and save the data to the database
        data = json.loads(request.body)
        
        event_mapping = {
            'email_click': ['email_id', 'timestamp', 'clicked_link'],
            'email_open': ['email_id', 'timestamp'],
            'email_unsubscribe': ['email_id', 'timestamp'],
            'purchase': ['email_id', 'timestamp', 'product_id', 'amount']
        }

        event_type = data.get('event_type')
        event_fields = event_mapping.get(event_type)

        if event_type and event_fields:
            event_data = {field: data.get(field) for field in event_fields}
            email_event = EmailEvent(
                customer_id=data['customer_id'],
                event_type=event_type,
                event_data=event_data
            )
            email_event.save()

            return JsonResponse({'message': 'Event received and saved successfully'})
        else:
            return JsonResponse({'message': 'Invalid event_type or missing event_fields'})
def get_events(request, customer_id):
    if request.method == 'GET':
        events = EmailEvent.objects.filter(customer_id=customer_id)
        data = [{'customer_id': event.customer_id, 'event_type': event.event_type, 'event_data': event.event_data, 'timestamp': event.timestamp} for event in events]
        return JsonResponse({'events': data})
