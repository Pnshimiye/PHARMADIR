from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_request_email(name,receiver):
    # Creating message subject and sender
    subject = 'Your request has been successfully sent'
    sender = 'pnshimiye@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/conf_email.txt',{"name": name})
    html_content = render_to_string('email/conf_email.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()