from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')

app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')
app.config_from_object('django.conf:settings', namespace='CELERY')

#celery beat settings

app.conf.beat_schedule = {
    #add task
    'send-mail-every-day-at-7':{
        'task':'email_sending.task.send_mail_func',
        'schedule':crontab(hour=18, minute=19),
      #  'args':()
    }
    
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

 
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')