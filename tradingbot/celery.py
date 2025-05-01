from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from redis import Redis

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tradingbot.settings')

app = Celery('tradingbot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Test Redis connection
redis_client = Redis(host='localhost', port=6379, db=0)