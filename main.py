import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

print("Connecting to smtp.gmail.com on port 587...")
server = smtplib.SMTP("smtp.gmail.com", 587)
print("Connected! Sending EHLO...")
server.ehlo()
print("Securing connection with TLS...")
server.starttls()
print("Sending EHLO again...")
server.ehlo()

with open("accounts.txt", "r") as f:
    email = f.readline().strip()
    password = f.readline().strip()

print(f"Logging in as {email}...")
server.login(email, password)
print("Logged in successfully!")


print("Preparing email headers...")
msg = MIMEMultipart()
msg['From'] = 'cyanide'
msg['To'] = 'ghostriley597@gmail.com'
msg['Subject'] = 'Test'

print("Reading body text from msg.txt...")
with open("msg.txt", "r") as f:
    body = f.read()

msg.attach(MIMEText(body, "plain"))

filename = 'pic.png'
print(f"Reading attachment {filename}...")
with open(filename, "rb") as attach:
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attach.read())

print("Encoding attachment...")
encoders.encode_base64(p)
p.add_header("Content-Disposition", f"attachment; filename= {filename}")

msg.attach(p)

text = msg.as_string()

print("Sending the email...")
server.sendmail(email, 'ghostriley597@gmail.com', text)
print("Email sent successfully!")
server.quit()
print("Session closed.")


