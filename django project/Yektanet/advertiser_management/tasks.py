# your_app/tasks.py

from celery import shared_task
from dateutil.relativedelta import relativedelta

from .models import click, ad, report_daily, view, report_hourly
from django.utils import timezone


@shared_task(bind=True)
def get_report_hourly(self):
    ads = ad.objects.all()
    current_time = timezone.now()

    one_hour_ago = current_time - timezone.timedelta(hours=1)
    for a in ads:
        clicks = click.objects.filter(created_on__range=[one_hour_ago, current_time], ad=a)
        views = view.objects.filter(created_on__range=[one_hour_ago, current_time], ad=a)
        report_hourly.objects.create(ad=a, clicks_count=len(clicks), views_count=len(views))


@shared_task(bind=True)
def get_report_daily(self):
    ads = ad.objects.all()
    current_time = timezone.now()

    one_day_ago = current_time - timezone.timedelta(days=1)
    for a in ads:
        clicks = sum(
            r.clicks_count for r in report_hourly.objects.filter(created_on__range=[one_day_ago, current_time], ad=a))
        views = sum(
            r.views_count for r in report_hourly.objects.filter(created_on__range=[one_day_ago, current_time], ad=a))
        report_daily.objects.create(ad=a, clicks_count=clicks, views_count=views)
