# code adapted from Yasaman and Colin

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import json
import urllib.parse as parse

def send_email(subject, sender, receiver):

    msg = MIMEMultipart("alternative")
    msg['Subject'] = subject
    msg['Subject'] = subject
    msg['From'] = sender
    if type(receiver) is list:
        msg['To'] = ", ".join(receiver)

    else:
        msg['To'] = receiver
    text = "This is an self generated email \n Do not reply to this message"
    part2 = MIMEText(text, "plain")

    # Add Plain - html to MIMEMultipart message
    msg.attach(part2)

    try:
        with smtplib.SMTP('mailserv.mmm.com') as smtp:
            smtp.sendmail(sender, receiver, msg.as_string())

    except Exception as e:
        print(f' error: {e}')