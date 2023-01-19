import smtplib;
import schedule;
import time;
from email.mime.multipart import MIMEMultipart;
from email.mime.text import MIMEText;
from email.mime.base import MIMEBase;
from email.mime.image import MIMEImage;
from email import encoders;
import os;
from dotenv import load_dotenv;

load_dotenv();
email_sender = os.getenv("EMAIL_SENDER");
email_pw = os.getenv("EMAIL_PW");
# Although this may not be required since I'm gonna loop it through the "list" but still ig, no harm in adding 1 more variable.
email_receiver = os.getenv("EMAIL_RECEIVER");
email_list = os.getenv("EMAIL_LIST");

def send_emails(email_list):
    for person in email_list:
        body = f'''
        <html>
        <body>
            <h1>Check out what's new!</h1>
            <br> 
            <p> <h4>Brought to you by <b>BloomReact</b></h4></p>
            <img src="/Users/mac/Desktop/Python/automated-email/1.email/final/static/saturn.jpeg" alt="Logo" \>
        </body>
        </html>
        ''';

        msg =MIMEMultipart();
        msg['From'] = email_sender;
        msg['To'] = person;
        msg['Subject'] = "We missed you!";

        msg.attach(MIMEText(body, 'html'));
        