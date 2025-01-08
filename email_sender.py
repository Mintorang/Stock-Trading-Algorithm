import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(sender_email, receiver_email, password, subject, body, csv_file_path):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject


    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))


    # Attach the CSV file
    if os.path.isfile(csv_file_path):
        with open(csv_file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(csv_file_path)}"
            )
            msg.attach(part)
    else:
        print("File not found!")
        
    # Set up the SMTP server and send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # For Gmail
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
