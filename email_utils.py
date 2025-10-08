import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_booking_email(to_email, booking):
    msg = EmailMessage()
    msg['Subject'] = 'Anandasna Yoga Booking Confirmation'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"Hi {booking.name},\n\nYour booking for {booking.class_type} is confirmed. Amount: ₹{booking.amount}\n\nThank you!")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
