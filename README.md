# Integration Hub

Integration Hub is a simple Django app that acts as an integration point for handling various email-related events. It provides a basic API to receive and query email events such as email clicks, opens, unsubscribes, and purchases.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- SQLite (Database)


### Installation and Running 

Navigate to the project directory:

```
cd integration-hub
```

Create a virtual environment (which is recommended):

```
python3 -m venv venv
```

Activate the virtual environment:

On macOS/Linux:
```
source venv/bin/activate
```


Intall dependecies: 
```
pip install -r requirements.txt
```
### Database Setup
The app uses SQLite as the default database, that way make sure to generate and run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Integration Hub uses SQLite as a lightweight and easy-to-set-up database solution. SQLite is suitable for small to medium-sized projects and simplifies the setup process for new contributors. Also, Django can create and manage the SQLite database automatically

### Then...
```
python manage.py runserver
```
The app will be accessible at http://localhost:8000/.


### Usage - Querying Events

```
Endpoint: http://127.0.0.1:8000/receive_event/
Method: POST
```

```
Endpoint: http://127.0.0.1:8000/get_events/{customer_id}
Method: GET
```


Examples: 

POST Examples, listening for events:

``` JSON
Endpoint: http://127.0.0.1:8000/receive_event/

Body: {
    "customer_id":  1112, 
    "event_type":  "email_open", 
    "timestamp":  "2023-10-24T11:30:00", 
    "email_id":  100
}
```

``` JSON
Endpoint: http://127.0.0.1:8000/receive_event/

Body: {
    "customer_id": 2223,
    "event_type": "email_click",
    "timestamp": "2023-10-23T14:30:00",
    "email_id": 1234,
    "clicked_link": "https://example.com/some-link"
}
```

``` JSON
Endpoint: http://127.0.0.1:8000/receive_event/

Body: {
    "customer_id": 999,
    "event_type": "email_unsubscribe",
    "timestamp": "2023-10-24T11:30:25",
    "email_id": 998
}
```

``` JSON
Endpoint: http://127.0.0.1:8000/receive_event/

Body: {
    "customer_id": 443,
    "event_type": "purchase",
    "timestamp": "25-10-2023T15:33:00",
    "email_id": 1234,
    "product_id": 357,
    "amount": 49.99
}
```



