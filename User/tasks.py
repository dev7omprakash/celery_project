import time
from celery import shared_task

from celery import shared_task
from django.core.mail import send_mail
import time


@shared_task(bind=True)
def send_mail_to_all_users(self, subject, message, sender, receiver):
    # operations
    time.sleep(20)  # for check that sending email process runs in background
    send_mail(subject, message, sender, receiver)
    return "Done"
