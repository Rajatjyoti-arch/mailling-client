import smtplib

# Recommended port for TLS is 587 (port 25 is often blocked by ISPs/firewalls)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls() # Secure the connection
server.ehlo()

# Load credentials from accounts.txt (which is ignored by Git to keep them hidden)
try:
    with open("accounts.txt", "r") as f:
        # Read lines and strip any surrounding whitespace/newlines
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