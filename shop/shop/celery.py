import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS-MODULE', 'shop.settings')

app = Celery('shop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks('django.conf:settings')


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

