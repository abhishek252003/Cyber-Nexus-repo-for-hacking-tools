import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set the sender and recipient email addresses
sender_email = "itzabhii2506@gmail.com"
recipient_email = "raijee0070071999@gmail.com"
password = "Abhishek2111"  # Replace with your actual password

# Create a MIMEMultipart message
logging.info("Creating email message...")
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Important Email"

# Add the message body as a MIMEText part
body = "This is the body of the email."
message.attach(MIMEText(body, "plain"))
logging.info("Attached message body.")

# Add an attachment as a MIMEApplication part
try:
    with open("attachment.pdf", "rb") as attachment_file:
        attachment = MIMEApplication(attachment_file.read(), _subtype="pdf")
        attachment.add_header("Content-Disposition", "attachment", filename="attachment.pdf")
        message.attach(attachment)
    logging.info("Attached file: attachment.pdf")
except FileNotFoundError:
    logging.error("Attachment file not found. Please ensure 'attachment.pdf' exists.")
    exit(1)

# Add headers to evade spam filters
message["X-Priority"] = "1"
message["X-MSMail-Priority"] = "High"
message["Importance"] = "High"
logging.info("Added headers to evade spam filters.")

# Send the email
try:
    logging.info("Connecting to SMTP server...")
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server:  # 10 seconds timeout
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        logging.info("Logging in to the email account...")
        server.login(sender_email, password)  # Login to your email account
        logging.info("Sending email...")
        server.sendmail(sender_email, recipient_email, message.as_string())
    logging.info("Email sent successfully!")
except Exception as e:
    logging.error(f"Failed to send email: {str(e)}")