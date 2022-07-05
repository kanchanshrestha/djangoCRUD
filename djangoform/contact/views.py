from django.conf import settings
from django.shortcuts import  render
from django.core.mail import send_mail
import smtplib
from django.core import mail

# Create your views here.
from django.core.mail import EmailMessage

def sendcontact(request):

    email = EmailMessage(
        subject = 'That’s your subject',
        body = 'That’s your message body',
        from_email = 'sudan@mailinator.com',
        to = ['kanchan@mailinator.com'],
       
    )
    email.send()


  # subject="test subject"
  # message="test message"
  # email_from=settings.EMAIL_HOST_USER
  # email_to="sudan1bhandari@gmail.com"
  # send_mail(subject,message,email_from,email_to)

    
    