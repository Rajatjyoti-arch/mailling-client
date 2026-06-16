# Mailing Client

A simple, straightforward mailing client written in Python that automates the process of sending emails with attachments via an SMTP server (like Gmail).

## Features

- **Automated Login:** Reads credentials from a local text file.
- **Message Body:** Reads the main message body from a local text file.
- **Attachments:** Capable of attaching binary files (like images) to the email.
- **Secure Connection:** Uses TLS (Transport Layer Security) for secure communication with the SMTP server.

## Code Overview & Libraries Explained

The script `main.py` relies on built-in Python libraries to construct and send the email. Here is a breakdown of the libraries and their roles in the codebase:

### 1. `smtplib`
The `smtplib` module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon. 
- In this script, it is used to connect to Gmail's SMTP server (`smtp.gmail.com`) on port 587.
- It initiates a secure TLS connection (`server.starttls()`), authenticates the user (`server.login()`), and ultimately sends the email (`server.sendmail()`).

### 2. `email` (and its submodules)
The `email` package is a library for managing email messages. It is used to construct the structure of the email, add headers, and manage attachments.

- **`email.mime.multipart.MIMEMultipart`**: This class is used to create a container for the email. Since the email contains both text and a binary attachment (an image), it needs to be a multipart email. The `MIMEMultipart` object acts as the root message to which other parts are attached.
- **`email.mime.text.MIMEText`**: This class is used to create MIME objects of major type text. In this script, it takes the plain text read from `msg.txt` and formats it appropriately so it can be attached to the `MIMEMultipart` container.
- **`email.mime.base.MIMEBase`**: The base class for all MIME-specific subclasses. It is used here to construct the attachment part for `pic.png`. It reads the file in binary mode (`rb`) and sets it as the payload with the type `application/octet-stream`.
- **`email.encoders`**: This module contains functions to encode payloads. Since `pic.png` is a binary file, it cannot be sent over SMTP as raw binary data. `encoders.encode_base64()` is used to encode the image data into Base64 format before attaching it to the email.

## How It Works

1. **Server Connection:** The script connects to `smtp.gmail.com:587` and upgrades the connection to secure TLS.
2. **Authentication:** It reads the sender's email and password from `accounts.txt` (first line is email, second line is password) and logs in.
3. **Constructing the Message:** 
   - A `MIMEMultipart` object is created to hold the email.
   - The sender (`From`), recipient (`To`), and `Subject` headers are set.
4. **Adding the Body:** The script reads the email body from `msg.txt` and attaches it as plain text.
5. **Adding the Attachment:** The script reads an image named `pic.png` in binary mode, encodes it in Base64, adds the necessary `Content-Disposition` header so it shows up as an attachment, and attaches it to the email.
6. **Sending:** The constructed message is converted to a string and sent via the SMTP server. Finally, the connection is closed.
