from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'invertirenbolsa.config.settings.local')

app = Celery('products', broker=settings.CELERY_BROKER_URL)

app.config_from_object('django.conf:global_settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-value-last-day': {
        'task': 'products.tasks.update_values',
        'schedule': crontab(minute=0, hour=4)
    },
}
