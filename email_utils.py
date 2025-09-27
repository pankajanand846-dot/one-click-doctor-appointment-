# email_utils.py
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
DOCTOR_EMAIL = os.getenv("DOCTOR_EMAIL")

def send_email(to_email=None, subject="", body=""):
    if to_email is None:
        to_email = DOCTOR_EMAIL  # fallback
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)

