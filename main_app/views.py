from .task import test_func
from django.http import HttpResponse
# from email_sending.task import send_mail_func
# Create your views here.


def test(request):
    test_func.delay()
    return HttpResponse("Done")


# def send_mail_to_all(request):
#     send_mail_func.delay()
#     return HttpResponse("Sent")