import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
DOCTOR_EMAIL = os.getenv("DOCTOR_EMAIL")

msg = EmailMessage()
msg["Subject"] = "Test Email from Hackathon App"
msg["From"] = EMAIL_USER
msg["To"] = DOCTOR_EMAIL
msg.set_content("Hello! This is a test email from your Doctor Appointment AI app.")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_USER, EMAIL_PASS)
    smtp.send_message(msg)

print("Email sent successfully!")
