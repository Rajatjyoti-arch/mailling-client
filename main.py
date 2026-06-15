import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls() 
server.ehlo()

try:
    with open("accounts.txt", "r") as f:
        email = f.readline().strip()
        password = f.readline().strip()

    if not email or not password:
        raise ValueError("Email or password in accounts.txt is empty.")

    server.login(email, password)
    print("Logged in successfully!")
except FileNotFoundError:
    print("Error: accounts.txt file not found. Please create one with your email and password.")
except Exception as e:
    print(f"Login failed: {e}")
finally:
    server.quit()