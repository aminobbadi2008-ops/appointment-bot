import os
import smtplib
from twilio.rest import Client

def send_notification(appointment, method):
    if method in ["sms", "both"]:
        send_sms(appointment)
    if method in ["email", "both"]:
        send_email(appointment)

def send_sms(appointment):
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    twilio_number = os.getenv("TWILIO_NUMBER")
    client = Client(account_sid, auth_token)

    message = f"Appointment confirmed with Dr. {appointment['dentist']} at {appointment['time_slot']} for a {appointment['type']}."
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=os.getenv("CUSTOMER_PHONE")
    )

def send_email(appointment):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    recipient = os.getenv("CUSTOMER_EMAIL")

    subject = "Dental Appointment Confirmation"
    body = f"Appointment confirmed with Dr. {appointment['dentist']} at {appointment['time_slot']} for a {appointment['type']}."

    email_text = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, email_text)