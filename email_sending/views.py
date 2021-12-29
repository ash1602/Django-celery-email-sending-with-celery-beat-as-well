from django.http import HttpResponse
from .task import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
# Create your views here.



def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 18, minute = 47)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task"+"2",
                                       task = "email_sending.task.send_mail_func")  # args = json.dumps((2,3)) 
    return HttpResponse( "done")
    