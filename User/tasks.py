import time

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_to_all_users(subject, message, sender, receiver):
 # for check that sending email process runs in background
    send_mail(subject, message, sender, receiver)
    return "Done"
