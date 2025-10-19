import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SENDER_EMAIL, SENDER_EMAIL_PASSWORD, RECIPIENT_EMAIL

def send_email(recipient, body,  subject="Application Letter"):
    #receiver_email = email if email != "No email found" else receiver_email

    msg = MIMEMultipart()
    msg["from"] =  SENDER_EMAIL
    msg["to"] =  recipient
    msg["subject"] =  subject
    msg.attach(MIMEText(body, "plain"))
    try:
        server =  smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient, msg.as_string())
        print(f"Email sent to {recipient} successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()
        
        
    