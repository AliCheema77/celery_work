from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from app.models import ScheduleTime
from datetime import datetime, timedelta


@shared_task
def send_mail_task_weekly():
    time_1 = datetime.now()
    time_2 = time_1 + timedelta(seconds=30)
    daily_thrashed = ScheduleTime.objects.filter(thrashed="weekly", schedule_time__gte=time_1, schedule_time__lte=time_2)
    subject = 'welcome to Celery world weekly'
    message = 'Hi thank you for using celery'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = []
    for user_email in daily_thrashed:
        recipient_list.append(user_email.email)
        user_email.schedule_time = user_email.schedule_time + timedelta(days=7)
        user_email.save()
    send_mail(subject, message, email_from, recipient_list)
    return "Mail has been sent weekly........"


@shared_task
def send_mail_task_daily():
    time_1 = datetime.now()
    time_2 = time_1 + timedelta(seconds=30)
    daily_thrashed = ScheduleTime.objects.filter(thrashed="daily", schedule_time__gte=time_1, schedule_time__lte=time_2)
    subject = 'welcome to Celery world daily'
    message = 'Hi thank you for using celery'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = []
    for user_email in daily_thrashed:
        recipient_list.append(user_email.email)
        user_email.schedule_time = user_email.schedule_time + timedelta(days=1)
        user_email.save()
    send_mail(subject, message, email_from, recipient_list)
    return "Mail has been sent daily........"



