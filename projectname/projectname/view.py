from django.http import HttpResponse
from .import settings
from django.core.mail import send_mail


def mail(request):
    subject = "Greetings"
    msg = "Congratulations for your success"
    to = "irfan.sssit@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if (res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)


import csv
