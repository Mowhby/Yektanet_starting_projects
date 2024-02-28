import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yektanet.settings')

app = Celery('Yektanet')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'save_data_hourly': {
        'task': 'advertiser_management.tasks.get_report_hourly',
        'schedule': crontab(minute=0, hour='*'),
    },
    'save_data_daily': {
        'task': 'advertiser_management.tasks.get_report_daily',
        'schedule': crontab(minute=0, hour=0),
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
