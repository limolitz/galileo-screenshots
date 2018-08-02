import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galileo_screenshots.settings')

app = Celery('galileo_screenshots')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
