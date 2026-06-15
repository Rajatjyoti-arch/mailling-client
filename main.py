import smtplib

server = smtplib.SMTP("smtp.gmail.com", 25)

server.ehlo()

with open("accounts.txt") as f:
    accounts = f.readlines()

server.login  