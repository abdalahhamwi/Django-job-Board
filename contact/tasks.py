from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email():

  send_mail(
    "mac",
    "Thank you for reaching out to us! We have successfully received your message. Our support team will carefully review your request and get back to you as soon as possible. We appreciate your patience and look forward to assisting you",
    "abdalah09941@gmail.com",
    ["abdalah09941@gmail.com"],
)
