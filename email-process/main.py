# Import smtplib for the actual sending function
from os import name
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '<Sender\'s name>'
email['to'] = '<Reciever\'s mail>'
email['subject'] = '<Subject to send>'

email.set_content(html.substitute({'name' : 'Ava'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<Enter sending email>', '<Enter sending email pass>')
    smtp.send_message(email)
    print("Sent")