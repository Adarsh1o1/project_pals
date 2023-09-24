from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings

def send_connect_mail(initiater, contributer,): 
    subject = 'connect'
    message = f'Hi {initiater}, {contributer} wants to connect with you, their email id is {contributer.email}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [initiater.email]
    send_mail(subject, message, email_from, recipient_list)
    return True