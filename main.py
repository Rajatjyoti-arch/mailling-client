import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 587)

server.ehlo()

with open("accounts.txt", "r") as f:
    email = f.readline().strip()
    password = f.readline().strip()

server.login(email, password)

msg = MIMEMultipart()
msg['From'] = 'cyanide'
msg['To'] = ''
