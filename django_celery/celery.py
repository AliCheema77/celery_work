from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')
app = Celery('django_celery')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')
app.conf.beat_schedule = {
    'Send_mail_weekly': {
        'task': 'app.tasks.send_mail_task_weekly',
        'schedule': 30.0,
    },
    'Send_mail_daily': {
        'task': 'app.tasks.send_mail_task_daily',
        'schedule': 30.0,
    },
}
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
