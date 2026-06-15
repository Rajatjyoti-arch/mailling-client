import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)

server.ehlo()

with open("accounts.txt", "r") as f:
    email = f.readline().strip()
    password = f.readline().strip()

server.login(email, password)
