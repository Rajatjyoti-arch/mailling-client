import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()

with open("accounts.txt", "r") as f:
    email = f.readline().strip()
    password = f.readline().strip()

server.login(email, password)

msg = MIMEMultipart()
msg['From'] = 'cyanide'
msg['To'] = 'ghostriley597@gmail.com'
msg['Subject'] = 'Test'

with open("msg.txt", "r") as f:
    body = f.read()

msg.attach(MIMEText(body, "plain"))

filename = 'pic.png'
with open(filename, "rb") as attach:
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attach.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f"attachment; filename= {filename}")

msg.attach(p)

text = msg.as_string()

server.sendmail(email, 'ghostriley597@gmail.com', text)
server.quit()
