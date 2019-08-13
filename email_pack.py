from flask_mail import Message
from flask import render_template
from app import mail
from app import app


# function of sending email
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


# send register confirm password
def send_register_email(account):
    token = account.get_register_token()
    send_email('Registration Verification',
               sender=app.config['ADMINS'][0],
               recipients=[account.account_email],
               text_body=render_template('email/register_template.txt', token=token),
               html_body=render_template('email/register_template.html', token=token)
               )


