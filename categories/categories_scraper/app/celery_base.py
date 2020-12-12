from celery import Celery
from celery import signature
import os

app = Celery()
app.conf.update({
    'task_routes': {
        'get_subcategories': {'queue': 'scraper'},
        'save_category': {'queue': 'mongo'}
    },
    'task_serializer': 'pickle',
    'result_serializer': 'pickle',
    'accept_content': ['pickle']
})

start_category = os.environ['main_category']

# save main category
x = signature(
    'save_category',
    args=[
        start_category,
        start_category,
        start_category,
        1
    ]
)
x.apply_async()

# run recurrent loop
x = signature(
    'get_subcategories',
    args=[
        start_category,
        start_category,
        start_category,
        1
    ]
)
x.apply_async()